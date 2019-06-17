# unit_price = float(input('输入商品单价：'))
# amounts = int(input('输入购买商品的数量:'))
# money = int(input('输入你支付了多少钱：'))
#
# Change = money - amounts * unit_price
#
# if Change >= 0:
#     print('找回%.2f元' % Change)
# else:
#     print('哎呀！！！钱不够啊！')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
获取一个季度（春夏秋冬）
显示相应的月份
春 1,2,3月
夏 4,5,6月
秋 7,8,9月
冬 10,11,12月
"""
# season = input('输入一个季度(春夏秋冬):')
# if season == "春":
#     print("一月二月三月")
# elif season == "夏":
#     print("四月五月六月")
# elif season == "秋":
#     print("七月八月九月")
# elif season == "冬":
#     print("十月十一月十二月")
# else:
#     print("输入有误！")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
录入一个数字，在录入一个运算符（+ - * /），再录入一个数字
根据运算符计算两个数字
如果运算符不是加减乘除，则提示运算符有误
"""
# number01 = float(input("输入第一个数字："))
# operator = input("输入一个运算符(+ - * /):")
# number02 = float(input("输入第二个数字："))
# if operator == "+":
#     print('%.2f + %.2f = %.2f' % (number01, number02, number01 + number02))
# elif operator == "-":
#     print('%.2f - %.2f = %.2f' % (number01, number02, number01 - number02))
# elif operator == "*":
#     print('%.2f * %.2f = %.2f' % (number01, number02, number01 * number02))
# elif operator == "/":
#     print('%.2f / %.2f = %.2f' % (number01, number02, number01 / number02))
# else:
#     print("请输入正确的运算符！")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
输入四个数字，打印最大的数字
"""
# number01 = int(input("第一个数字："))
# number02 = int(input("第二个数字："))
# number03 = int(input("第三个数字："))
# number04 = int(input("第四个数字："))
# max_number = number01
# if number02 > max_number:
#     max_number = number02
# if number03 > max_number:
#     max_number = number03
# if number04 > max_number:
#     max_number = number04
# print("最大数是：", max_number)
"""
冒泡排序
"""
# number_list = [5, 8, 4, 6, 9, 1, 34, 9, 65, 8, 88, 45]
# print(number_list)
# for i in range(len(number_list)):
#     for j in range(i + 1, len(number_list)):
#         if number_list[j] > number_list[i]:
#             number_list[i], number_list[j] = number_list[j], number_list[i]
#     print(number_list)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
录入成绩，判断等级（优秀/良好/及格/不及格/输入有误）
"""
# grade = int(input("输入成绩(0-100):"))
#
# if 0 <= grade <= 100:
#     if grade >= 90:
#         print("优秀")
#     elif grade >= 80:
#         print("良好")
#     elif grade >= 60:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("输入有误")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
month = int(input("输入一个月份："))
if 1 <= month <= 12:
    if month == 2:
        print("有28天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("有30天")
    else:
        print("有31天")
else:
    print("输入错误")
