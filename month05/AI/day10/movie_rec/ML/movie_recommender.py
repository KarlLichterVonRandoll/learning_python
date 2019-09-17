import pandas as pd
import numpy as np
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity


def init_common_similarity_matrics():
    # 初始化普通推荐模型的相似用户矩阵
    u_score = pd.read_csv('basedata/u_score.csv', header=None)
    m_type = pd.read_csv('middata/tag.csv', header=None).drop([0], axis=1)
    # 得到用户真实id
    users_id = u_score.loc[:, 1]
    # 用户id去重
    users_id = users_id.drop_duplicates(keep='first', inplace=False)
    # 将电影类型存, 用户标签入列表，方便拿索引
    type_list = []
    tag_list = []
    for i, j in zip(m_type.loc[:, 1], m_type.loc[:, 2]):
        type_list.append(i)
        tag_list.append(j)
    # 得到用户真实id列表
    users_id_list = []
    for user_id in users_id:
        users_id_list.append(user_id)
    i_list = []
    j_list = []
    user_type = pd.DataFrame(np.zeros(shape=(len(users_id_list), 32)))
    for i, u_id in enumerate(users_id):
        l = []
        for n in range(len(u_score)):
            if u_id == u_score.loc[n, 1]:
                for type in u_score.loc[n, 3:6]:
                    l.append(type)
        num_list = Counter(l)
        # print(num_list)
        for type in num_list:
            # print(type)
            if type in type_list:
                j = type_list.index(type)
                # print(j)
                i_list.append(i)
                j_list.append(j)
                user_type.loc[i, j] = 1
    # print(user_type)
    # # 得到用户相似度矩阵
    similarity_tabel = cosine_similarity(user_type, user_type)
    # print(similarity_tabel)
    # print(u_score)
    return u_score, users_id_list, user_type, similarity_tabel, type_list


# 普通推荐模型
class CommonRecommendModel:
    u_score, users_id_list, user_type, \
    similarity_tabel, type_list = init_common_similarity_matrics()

    def recommend_by_userid(self, uid):
        # 传入userid 根据 userid 获取喜欢的电影类型 -> mtypes
        i = self.users_id_list.index(uid)
        mtypes = []
        for type_index, type in enumerate(self.user_type.loc[i]):
            if type != 0:
                mtypes.append(self.type_list[type_index])
            # print(mtypes)
        return self.recommend(mtypes, i, uid)

    def recommend(self, mtype, i, uid):
        # 传入喜欢的电影类型，根据data给出推荐结果
        s_list = []
        for j in range(len(self.user_type)):
            s_list.append(self.similarity_tabel[i, j])
        # 将用户（包含该用户本身）根据相似度由高到低进行排序
        sim = -np.sort(-self.similarity_tabel[i])
        # 排序结果的[1:6]为与其相似度最高的五个用户的相似度，根据相似度可以得到相似用户的索引
        sim_uid = []  # 存放相似用户的id
        movies_score = {}  # 创建字典{电影ID:评分}
        for j in range(1, 6):
            movies_id = []  # 该相似用户看过的电影
            score_list = []  # 该相似用户对电影的评分
            index = s_list.index(sim[j])  # 得到相似用户的索引
            s_uid = self.users_id_list[index]  # 根据用户索引在用户列表中俺找到用户id
            sim_uid.append(s_uid)
            # print(s_uid)
            # 找相似用户看过的电影和评分
            for n in range(len(self.u_score)):
                if s_uid == self.u_score.loc[n, 1]:
                    movies_id.append(self.u_score.loc[n, 0])
                    score = int(self.u_score.loc[n, 2])  # 用户对电影的评分
                    score_list.append(score)  # 得到电影评分列表
            # 对电影评分进行处理
            score_array = np.array(score_list)
            score_std = np.std(score_array)
            score_ave = np.mean(score_array)
            score_fina = []
            for s in score_list:
                score = (s - score_ave) / score_std  # 归一化
                score_fina.append(score)
            for movie, score in zip(movies_id, score_fina):
                movies_score[score] = movie  # # 字典排序，sorted函数，根据键排序
        # print('用户id为', uid, '相似的5个用户id为：', sim_uid, '看过的所有电影ID和评分：', movies_score)
        movies_score = sorted(movies_score.items())[0:10][::-1]
        rec_movies_id = []
        for movie_score in movies_score:
            rec_movies_id.append(movie_score[1])
        print('用户id为', uid, '相似的5个用户id为：', sim_uid, '推荐的所有电影ID：', rec_movies_id)
        return np.unique(rec_movies_id)
