"""
    列表 -->  字典
"""
# dict01 = {}
# for item in ["无极", "赵敏", "周芷若"]:
#     dict01[item] = 3 if item == "周芷若" else 2
# print(dict01)
#
# list01 = ["无极", "赵敏", "周芷若"]
# list02 = [101, 102, 103]
#
# dict02 = {list01[i]:list02[i] for i in range(3)}
# print(dict02)


"""
    循环录入字符串，输入空字符停止
    打印所有不重复的文字
"""
# str_set = set()
# while True:
#     str_input = input("输入一个字符：")
#     if str_input == "":
#         break
#     str_set.add(str_input)
# print(str_set)

"""
    经理：曹操，刘备，孙权
    技术：曹操，刘备，张飞，关羽
    计算（1）是经理也是技术的有谁  （2）石经理，不是技术的有谁  （3） 是技术，不是经理的有谁
    （4） 张飞是经理艾玛  （5）生煎一直的有谁  （6）尽力和技术总共有多少人
"""
# set01 = {"曹操", "刘备", "孙权"}
# set02 = {"曹操", "刘备", "关羽", "张飞"}
# print("是经理也是技术的有", set01 & set02)
# print("石经理，不是技术的有", set01 - set02)
# print("是技术，不是经理的有", set02 - set01)
# print("张飞是经理吗？", "张飞" in set01)
# print("生煎一直的有", set01 ^ set02)
# print("经理和技术总共有", len(set01 | set02))


