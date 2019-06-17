"""
    输入日期(年月），输出一年中的第几天，借助元组
    例如： 3月5日
          1月天数 + 2月天数 + 5
"""
# month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# month = int(input("输入月份(1-12)："))
# day = int(input("输入日期(1-31)："))
# total_days = 0
# # 方法一
# for item in range(month - 1):
#     total_days += month_tuple[item]
# print("这是一年中的第%d天" % (total_days + day))
# # 方法二
# print("这是一年中的第%d天" % (sum(month_tuple[:month-1]) + day))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    循环录入商品信息(名称，单价）
    如果名称录入空字符，则停止录入
    将信息逐行打印
"""
# dict01 = {}
# while True:
#     name = input("输入商品名称:")
#     if name == "":
#         break
#     price = input("输入商品单价：")
#     dict01[name] = price
#
# for item in dict01:
#     print("%s 单价为 %s $" % (item, dict01[item])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    录入学生信息 （姓名，年龄，成绩，性别）
    输入空字符，则停止输入，打印信息
"""
# dict_student_info = {}
# while True:
#     name = input("输入学生姓名：")
#     if name == "":
#         break
#     # dict_student_info[name] = {}
#     age = input("输入学生年龄：")
#     score = input("输入学生成绩：")
#     sex = input("输入学生性别：")
#     dict_student_info[name] = {"age": age, "score": score, "sex": sex}
#
# for item in dict_student_info.items():
#     print(item)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    列表内嵌字典
"""
# list_student_info = []
# while True:
#     name = input("输入学生姓名：")
#     if name == "":
#         break
#     age = input("输入学生年龄：")
#     score = input("输入学生成绩：")
#     sex = input("输入学生性别：")
#     dict_student_info = {"name": name, "age": age, "score": score, "sex": sex}
#     list_student_info.append(dict_student_info)
#
# for item in list_student_info:
#     print(item)
#
# print(list_student_info)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    录入多个人的多个喜好
"""
# people_dict = {}
# while True:
#     name = input("输入姓名：")
#     if name == "":
#         break
#     list_hobby = []
#     while True:
#         hobby = input("输入你的第%d个喜好:" % (len(list_hobby) + 1))
#         if hobby == "":
#             break
#         list_hobby.append(hobby)
#     people_dict[name] = list_hobby
#
# for k, v in people_dict.items():
#     print("%s的喜好有%s" % (k, v))

list01 = []
for i in range(100, 1000):
    number01 = i // 100
    number02 = i % 100 // 10
    number03 = i % 10
    if number01**3 + number02**3 + number03**3 == i:
        list01.append(i)
print(list01)
print(sum(list01))

