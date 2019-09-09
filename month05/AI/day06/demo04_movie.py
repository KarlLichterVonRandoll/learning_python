"""
电影推荐
"""

import json
import numpy as np

with open('../ml_data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())
# 所有用户列表
users = list(ratings.keys())
# 整理相似度得分矩阵
scmat = []
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        for movie in ratings[user1]:
            if movie in ratings[user2]:
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        else:  # 两人有共同看过的电影
            A, B = [], []
            for movie in movies:
                A.append(ratings[user1][movie])
                B.append(ratings[user2][movie])
            # 计算两人的相似度
            A = np.array(A)
            B = np.array(B)
            # 欧式距离得分
            # score = np.sqrt(((A - B)**2).sum())
            # score = 1 / (1 + score)
            # 皮式距离得分 （皮尔逊相关系数）
            score = np.corrcoef(A, B)[0, 1]

        scrow.append(score)
    scmat.append(scrow)
print(np.round(scmat, 2))

# 召回操作 为每一个人找到所有的推荐电影
# 找到相似用户、按照相似度从高-低排序
scmat = np.array(scmat)
users = np.array(users)
for i, user in enumerate(users):
    sorted_indics = scmat[i].argsort()[::-1]
    sorted_indics = sorted_indics[sorted_indics != i]
    sim_users = users[sorted_indics]
    sim_scores = scmat[i, sorted_indics]
    # print(user, sim_users, sim_scores)
    # 生成推荐清单
    pos_mask = sim_scores > 0
    sim_users = sim_users[pos_mask]
    # 使用字典存储最终推荐清单
    # {'哪吒':[9.0, 7.9], '复联4':[8.0, 9.0, 8.0]..}
    recomm_movies = {}
    for i, sim_user in enumerate(sim_users):
        for movie, score in ratings[sim_user].items():
            if movie not in ratings[user].keys():
                # movie为推荐电影
                if movie not in recomm_movies:
                    recomm_movies[movie] = [score]
                else:
                    recomm_movies[movie].append(score)

    print(user)
    # 针对结果清单进行排序 (value的均值)
    movie_list = sorted(
        recomm_movies.items(),
        key=lambda x: np.average(x[1]),
        reverse=True)
    print(movie_list)
