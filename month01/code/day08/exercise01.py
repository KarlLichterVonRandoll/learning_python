"""
    计算四位整数，每位相加和的函数
"""

# def each_unit_sum(number):
#     """
#         计算整数每位相加的和
#     :param number: 四位整数
#     :return:
#     """
#     # 累加千位
#     result = number // 1000
#     # 累加百位
#     result += number // 100 % 10
#     # 累加十位
#     result += number % 100 // 10
#     # 累加个位
#     result += number % 10
#     return result
#
#
# print(each_unit_sum(1234))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数，根据两计算几斤几辆
"""

# def compute_weight(weight):
#     """
#         根据两计算几斤几两
#     :param weight: 几两
#     :return: 元组（斤数，两数）
#     """
#     weight_jin = weight // 16
#     weight_liang = weight % 16
#     return weight_jin, weight_liang
#
#
# jin, liang = compute_weight(12138)
# print(type(compute_weight()))
# print("%d斤零%d两" % (jin, liang))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数，根据成绩定义等级
"""

# def score_to_level(score):
#     """
#         根据成绩定义等级
#     :param score: 成绩(0-100)
#     :return:  等级
#     """
#     if 0 <= score <= 100:
#         if score >= 90:
#             print("优秀")
#         elif score >= 80:
#             print("良好")
#         elif score >= 60:
#             print("及格")
#         else:
#             print("不及格")
#     else:
#         print("成绩有误")
#
#
# score_to_level(90)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数，判断列表中有没有相同元素
"""

# def same_element(list01):
#     """
#         判断列表中有没有相同元素
#     :param list01: 判断列表
#     :return: True or False
#     """
#     for i in range(len(list01) - 1):
#         for j in range(i + 1, len(list01)):
#             if list01[i] == list01[j]:
#                 return True
#     return False
#
#
# re = same_element([1, 2, 3, 4])
# print(re)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数，输入年月计算有多少天，考虑闰年29 天
"""

# def is_leap_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def calculate_days(year, month):
#     """
#         输入年月计算有多少天，考虑闰年29 天
#     :param year: 年份
#     :param month:  月份
#     :return:  天数
#     """
#     if 1 <= month <= 12:
#         if month == 2:
#             return 29 if is_leap_year(year) else 28
#         if month in (4, 6, 9, 11):
#             return 30
#         return 31
#     else:
#         return -1
#
#
# re = calculate_days(2021, 2)
# print(re)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义列表升序排列的函数
"""

# def sort(list01):
#     """
#         将列表升序排列
#     :param list01:  列表 list
#     :return:  排序后的列表 list
#     """
#     for i in range(len(list01) - 1):
#         for j in range(i + 1, len(list01)):
#             if list01[i] > list01[j]:
#                 list01[i], list01[j] = list01[j], list01[i]
#
#
# list01 = [9, 8, 7, 6, 5]
# sort(list01)
# print(list01)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    方阵转置函数
"""

# def transposition(matrix_input):
#     """
#         方阵转置
#     :param matrix_input:  方阵
#     :return:  None
#     """
#     for i in range(len(matrix_input)):
#         for j in range(i + 1, len(matrix_input)):
#             matrix_input[i][j], matrix_input[j][i] = matrix_input[j][i], matrix_input[i][j]
#
#
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# transposition(list01)
# for item in list01:
#     print(item)
# transposition(list01)
# for item in list01:
#     print(item)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    统计函数执行次数
"""

# count = 0
#
#
# def func():
#     global count
#     count += 1
#
#
# func()
# func()
# func()
# func()
# func()
# func()
# func()
# print(count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    根据小时，分钟，秒，计算总秒数
"""

# def calculate_seconds(hours=0, minutes=0, seconds=0):
#     """
#         根据小时，分钟，秒，计算总秒数
#     :param hours:  小时 int
#     :param minutes:   分钟 int
#     :param seconds:   秒 int
#     :return:   总秒数
#     """
#     return hours * 3600 + minutes * 60 + seconds
#
#
# results = calculate_seconds(1, 1, 1)
# print(str(results) + "秒")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义数值相加的函数
"""


# def add(a, *args, b):
#     sum = a
#     for item in args:
#         sum += item
#     return sum
#
#
# print(add(1, 3, 4, 4, 5, b=2))

