import pandas as pd
import numpy as np
import sklearn.cluster as sc
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier


# 得到数据
def get_data():
    data = pd.read_csv('../terdata/u_bool_type.csv', header=None)
    data = data.drop([0], axis=1)
    m_type = pd.read_csv('../middata/m_type.csv', header=None)
    u_id = pd.read_csv('../middata/u_idx.csv', header=None)
    u_id = u_id.drop([0], axis=1)
    u_score = pd.read_csv('../basedata/u_score.csv', header=None)
    m_name = pd.read_csv('../basedata/m_name.csv', header=None)
    return data, m_type, u_id, u_score, m_name


# k-means 做用户聚类
def train_model(data):
    data = np.array(data)
    model = sc.KMeans(n_clusters=5)
    model.fit(data)
    pred_c = model.predict(data)
    return pred_c


# knn 依据用户标签找相邻用户
def neighbors(data, pred_c, new_user):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(data, pred_c)
    n_knn = knn.predict(new_user)
    y, idx = knn.kneighbors(new_user, n_neighbors=5)
    print("距离新用户距离最近的用户:", idx)
    return idx


# 得到近邻用户喜爱的电影类型
def get_type(data, idx, m_type):
    type = []
    # 遍历每一个相似用户
    for i in idx[0]:
        for ind, t in enumerate(data.loc[i]):
            if t == 1:
                type.append(m_type.loc[ind, 1])
    dict_type_num = Counter(type)
    print(dict_type_num)
    return dict_type_num


# 依据电影类型找电影，将用户没有看过的电影推荐给他
def get_movies(idx, u_id, u_score, m_name):
    print(type(u_id))
    for i in idx[0]:
        movie_list = []
        user = u_id.loc[i, 1]  # user的真实id
        for i in range(len(u_score)):
            if user == u_score.loc[i, 1]:
                m_id = u_score.loc[i, 0]  # 相似用户看过的电影id
                for i in range(len(m_name)):
                    if m_id == m_name.loc[i, 0] and m_name.loc[i, 1] not in movie_list:
                        movie_list.append(m_name.loc[i, 1])
        print("用户ID为:", user)
        print("看过的电影:", movie_list)


def main():
    new_user = [[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1,
                 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
    data, m_type, u_id, u_score, m_name = get_data()
    pred_c = train_model(data)
    # u_tag(pred_c)
    idx = neighbors(data, pred_c, new_user)
    dict_type_num = get_type(data, idx, m_type)
    get_movies(idx, u_id, u_score, m_name)


main()