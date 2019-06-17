"""
    真值表达式
    条件表达式
"""
# 1.真值表达式
# if bool(0):
#     print('True')
# else:
#     print('False')
#
# # 2.条件表达式：有选择性的为变量赋值
# sex = 1 if input("输入性别：") == "男" else 0
# print(sex)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
获取一个帧数
如果是偶数，则变量state赋值为”偶数“，否则赋值为”奇数“
"""
# state = "奇数" if int(input("输入一个数：")) % 2 else "偶数"
# print(state)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# year = int(input("输入一个年份："))
# day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# print(day)

"""
while 循环
"""
# while True:
#     season = input("输入一个季度")
#     if season == 'q':
#         break
#     elif season == '春':
#         print("春眠不觉晓")
#     elif season == '夏':
#         print("夏天")
#     elif season == '秋':
#         print("七月")
#     elif season == '冬':
#         print("dong")
#     else:
#         print("error")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
i = 0
while i < 6:
    print(i)
    i += 1

i = 2
while i < 8:
    print(i)
    i += 1

i = 0
while i < 7:
    if i % 2 == 0:
        print(i)
    i += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


