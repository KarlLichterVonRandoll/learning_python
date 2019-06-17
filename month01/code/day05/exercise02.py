"""
    1.将列表[1,3,4,5,6,...,5]中
    大于 30 的数存入另一个列表
    并画出内存图
"""
# list01 = [28,99999,7,12,34,66,8,9]
# list02 = []
# for i in list01:
#     if i > 30:
#         list02.append(i)
# print(list02)
# print(id(list01[1]))
# print(id(list02[0]))
# list01[1] = 0
# print(id(list01[1]))
# print(id(list02[0]))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    2.录入 5 个数字
    打印最大值，不使用 max.
"""
# max = int(input("输入第%d个数:" % 1))
# for i in range(4):
#     number = int(input("输入第%d个数:" % (i + 2)))
#     if number > max:
#         max = number
# print("最大为" + str(max))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    3.在列表[54,56,7,-9,7,87,4]中选出最大值
"""

# list01 = [54,56,7,-9,7,87,4]
# max_value = list01[0]
#
# for item in range(1, len(list01)):
#     if list01[item] > max_value:
#         max_value = list01[item]
# print(max_value)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    4.在列表[9,25,12,8],删除大于10的数
"""
# remove 删除一个元素后会被后面的元素覆盖
# 所以要从后往前删
# list01 = [9,25,12,8]
# for i in range(len(list01)-1,-1,-1):
#     if list01[i] > 10:
#         list01.remove(list01[i])
# print(list01)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    5.循环输入字符串，如果为空则停止
    最后打印所有内容（拼接后的字符串）
"""
# str_list = []
# while True:
#     str_unit = input("输入一个字符串：")
#     if str_unit == "":
#         print("".join(str_list))
#         break
#     str_list.append(str_unit)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    6.英文单词翻转
    “How are you" --> "you are How"
"""
# str01 = "How are you"
# str01_list = str01.split(" ")
# str02 = " ".join(str01_list[::-1])
# print(str02)
