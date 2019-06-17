"""
    1.录入西游记中的任务,输入空字符串，打印所有人物（一行一个）
"""
# list01 = []
# while True:
#     c = input("输入一个西游记的人物：")
#     if c == "":
#         for item in list01:
#             print(item)
#         break
#     list01.append(c)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    2.录入学生成绩，输入空字符串，打印所有成绩、最高分、最低分、平均分
"""
# score = []
# while True:
#     c = input("输入一个学生的成绩：")
#     if c == "":
#         for item in score:
#             print(item)
#         print("最高分是%.2f,最低分%.2f,平均分%.2f"
#               % (max(score), min(score), sum(score) / len(score)))
#         break
#     score.append(float(c))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    3.录入所有学生姓名，如果姓名重复，则提示已经存在，不添加到列表中
    如果录入空字符串，则倒序打印
"""
# name_list = []
# while True:
#     c = input("输入一个学生的姓名：")
#     if c == "":
#         for i in range(len(name_list)-1,-1,-1):
#             print(name_list[i])
#         break
#     elif c not in name_list:
#         name_list.append(c)
#         continue
#     print("姓名已存在")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import copy
# list01 = [500,[600,700]]
# list03 = copy.deepcopy(list01)
# list01[0] = 980
# print(list01)  # [980, [600, 700]]
# print(list03)  # [500, [600, 700]]
# list01[1][0] = 855
# print(list01)  # [980, [855, 700]]
# print(list03)  # [500, [855, 700]]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


