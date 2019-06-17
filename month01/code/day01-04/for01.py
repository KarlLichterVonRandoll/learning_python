"""
for 适合指定次数
for 变量列表 in 可迭代对象 :
"""
# str01 = "我叫苏大强"
#
# for item in str01:
#     print(item)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
整数生成器： range(开始值，结束值，间隔)
for + range : 善于执行预定次数
"""
# for item in range(1, 5, 2):
#     print(item)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
累加 1 到 100 的和
累加 1 到 100 之间偶数的和
累加 10 到 36 之间的和
"""
# sum01, sum02, sum03 = 0, 0, 0
# for i in range(101):
#     sum01 += i
#     sum02 += i if i % 2 == 0 else 0
#
# for i in range(10, 37):
#     sum03 += i
#
# print(sum01, sum02, sum03)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
随机加法，随机产生两个数字（1-10)
获取两个数相加的结果
如果用户输入正确得十分，总共3道题
例如：8+3=？  10   不得分
     4+3=？  7    得十分
输出总得分
"""
# import random
#
# score = 0
# for i in range(3):
#     number01 = random.randint(1, 100)
#     number02 = random.randint(1, 100)
#     summation = number01 + number02
#     answer = int(input("输入:%d+%d=? " % (number01, number02)))
#     if answer == summation:
#         print("得十分")
#         score += 10
#     else:
#         print("不得分")
# print("总得分为%d" % score)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
获取一个整数，判断是否为素数
"""
# from math import sqrt
#
# number = int(input("输入一个整数："))
# if number <= 1:
#     print("不是素数")
# else:
#     for i in range(2, int(sqrt(number)+1)):
#         if number % i == 0:
#             print("不是素数")
#             break
#     else:
#         print("是素数")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
累加10--50之间个位不是2,5,9的整数
"""
# summation = 0
# for item in range(10, 51):
#     if item % 10 == 2 or item % 10 == 5 or item % 10 == 9:
#         continue
#     summation += item
# print(summation)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
