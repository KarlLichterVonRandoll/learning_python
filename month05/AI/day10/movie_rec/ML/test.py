import numpy as np
import pandas as pd
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity


class MovieRec:
    def __init__(self):
        # 读取用户观看电影记录，包括评分，电影类型
        self.u_score = pd.read_csv("../basedata/u_score.csv", header=None)
        # print(self.u_score)
        # 读取电影类型文件，以及对应的用户标签
        m_type = pd.read_csv("../middata/tag.csv", header=None)
        self.m_type = m_type.drop([0], axis=1)
        # print(self.m_type)

    def get_list(self):
        '''
        将各个属性存入列表，为之后根据索引获取元素值做准备
        :return: type_list 电影类型列表
                 tag_list  标签列表
                 users_id_list 用户真实id列表
        '''
        users_id = self.u_score.loc[:, 1]
        users_id = users_id.drop_duplicates(keep="first", inplace=False)  # 用户id去重

        # 将电影类型存入列表，方便拿索引
        type_list = []
        for i in self.m_type.loc[:, 1]:
            type_list.append(i)
        # print(type_list)

        # 获取标签列表
        tag_list = []
        for i in self.m_type.loc[:, 2]:
            tag_list.append(i)
        # print(tag_list)

        # 得到用户真实id列表
        users_id_list = []
        for user_id in users_id:
            users_id_list.append(user_id)
        # print(users_id_list)

        return type_list, tag_list, users_id_list

    def get_user_tag(self):
        """
        生成401行32列数据表
        行为用户id，列为标签名，值为各个标签所占权重
        :return: user_tag 用户-标签
                 i_list ：用户索引总列表
                 j_list： 用户看过的电影类型的索引总列表
                 weight_list:电影权重列表
        """
        type_list, tag_list, users_id_list = self.get_list()
        # 生成 user_tag 表
        user_tag = pd.DataFrame(np.zeros(shape=(len(users_id_list), 32)))

        i_list = []  # 存放用户id对应在user_tag中的行号
        j_list = []  # 标签在user_tag中对应的列号
        weight_list = []  # 电影权重列表
        for i, u_id in enumerate(users_id_list):  # i 为user_tag的行标
            l = []
            for n in range(len(self.u_score)):
                if u_id == self.u_score.loc[n, 1]:
                    for type in self.u_score.loc[n, 3:6]:
                        l.append(type)
            num_list = Counter(l)  # {'剧情': 9, nan: 6, '犯罪': 5, '爱情': 4, '喜剧': 4, '音乐': 2, '动作': 2, '传记': 2, '家庭': 2}

            for weight_t in num_list:  # weight_t 表示电影类型
                if weight_t in type_list:
                    j = type_list.index(weight_t)  # 找到该类型在user_tag中对应的列标
                    i_list.append(i)
                    j_list.append(j)
                    weight_list.append(num_list[weight_t])
                    user_tag.loc[i, j] = float(num_list[weight_t])
        user_tag.columns = tag_list
        # print(user_tag)

        return user_tag, i_list, j_list, weight_list

    def get_tag_table(self):
        """
        得到列名分别为u_index,tag_id,weight 的表
        :return:
        """
        user_tag, i_list, j_list, weight_list = self.get_user_tag()
        tag_table = pd.DataFrame(np.zeros(shape=(len(i_list), 3)))
        for num in range(len(i_list)):
            tag_table.loc[num, 0] = float(i_list[num])
            tag_table.loc[num, 1] = float(j_list[num])
            tag_table.loc[num, 2] = float(weight_list[num])

        tag_table.columns = ['u_index', 'tag_id', 'weight']
        return tag_table

    def get_sim_table(self):
        user_tag, i_list, j_list, weight_list = self.get_user_tag()
        # 得到用户相似度矩阵
        user_tag_array = np.array(user_tag)
        similarity_table = cosine_similarity(user_tag, user_tag)

        return similarity_table

    def get_sim_id(self, index, users_id_list, id):
        # 相似用户id
        s_uid = users_id_list[index]
        movies_id = []
        for n in range(len(self.u_score)):
            if s_uid == self.u_score.loc[n, 1]:
                movies_id.append(self.u_score.loc[n, 0])
        m_name = pd.read_csv("../basedata/m_name.csv", header=None)
        movies = []
        for l in range(len(m_name)):
            if m_name.loc[l, 0] in movies_id:
                movies.append(m_name.loc[l, 1])
        print('用户id为：', id, '相似用户id为：', s_uid, '推荐的电影:', movies)

    def test_login(self):
        """
          测试：已存在用户
        """
        user_tag, i_list, j_list, weight_list = self.get_user_tag()
        type_list, tag_list, users_id_list = self.get_list()
        similarity_table = self.get_sim_table()
        id = input("输入用户id:")
        i = users_id_list.index(id)
        print(i)
        print(user_tag.loc[i])
        print("用户标签为:")
        for tag_index, tag in enumerate(user_tag.loc[i]):
            if tag != 0:
                print(tag_list[tag_index])
        s_max = 0
        s_list = []
        for j in range(len(user_tag)):
            s_list.append(similarity_table[i, j])
            if i != j:
                if s_max <= similarity_table[i, j]:
                    s_max = similarity_table[i, j]
        print("最大相似度:", s_max)
        index = s_list.index(s_max)
        self.get_sim_id(index, users_id_list, id)

    def test_new(self):
        user_tag, i_list, j_list, weight_list = self.get_user_tag()
        type_list, tag_list, users_id_list = self.get_list()
        new_user_type = input('请输入喜欢的类型对应的序号，以空格分隔：')
        new_user_type = new_user_type.split(" ")
        new_user = []
        for new in new_user_type:
            new_user.append(int(new))
        print("用户标签:")
        for m in new_user:
            print(tag_list[m])
        print('通过用户选择的电影类型为用户打上标签，得到包含31个元素的列表')
        new_list = []
        for m in range(len(type_list)):
            if m in new_user:
                new_list.append(1)
            else:
                new_list.append(0)
        print(new_list)
        user_tag.loc[len(user_tag)] = new_list  # 将新用户加入到用户列表中
        print(user_tag)
        similarity_table = cosine_similarity(user_tag, user_tag)
        print("得到新用户和其他用户的相似度")
        i = len(user_tag) - 1
        s_max = 0
        s_list = []
        for j in range(len(user_tag)):
            s_list.append(similarity_table[i, j])
            if i != j:
                if s_max <= similarity_table[i, j]:
                    s_max = similarity_table[i, j]
        print("最大相似度：", s_max)
        index = s_list.index(s_max)
        self.get_sim_id(index, users_id_list, id)


if __name__ == '__main__':
    movies_rec = MovieRec()
    num = input('是否存在用户id？y/n:')
    if num == 'y':
        movies_rec.test_login()
    else:
        movies_rec.test_new()
