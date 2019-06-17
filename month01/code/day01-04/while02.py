"""
获取一个开始值，一个结束值
将中间的数字打印出来
"""
# start = int(input("输入开始值："))  # 3
# end = int(input("输入结束值："))  # 10
# start += 1
# while start < end:
#     print(start)
#     start += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
一张纸厚度为0.01mm
计算对折多少次超过珠穆朗玛峰。
"""
# thickness = 0.01
# height = 8844.43e3
# count = 0
# while thickness < height:
#     thickness *= 2
#     print(thickness)
#     count += 1
#
# print(count)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
猜数字：产生一个1-100的随机数
重复猜，直到猜对为止，提示大了还是小了
"""
# import random
#
# random_number = random.randint(1, 100)
# print(random_number)
# count = 0
# while count < 3:
#     input_number = int(input("输入数字(1-100):"))
#     count += 1
#     if input_number == random_number:
#         print("猜对了！总共猜了%d次" % count)
#         break
#     elif input_number > random_number:
#         print("猜大了！")
#     else:
#         print("猜小了！")
# else:
#     print("游戏结束")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
根据成绩判断等级，如果录入空字符则退出程序
错误超过 3 次，则退出成绩并提示错误过多
"""
# count = 0
# while count < 3:
#     grade = input("输入成绩(0-100):")
#     if grade == '':
#         break  # 不会执行else语句
#     grade = int(grade)
#     if 0 <= grade <= 100:
#         if grade >= 90:
#             print("优秀")
#         elif grade >= 80:
#             print("良好")
#         elif grade >= 60:
#             print("及格")
#         else:
#             print("不及格")
#     else:
#         print("输入有误")
#         count += 1
# else:
#     print("错误次数太多!")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
