"""
录入商品单价
再录入数量
最后获取金额，计算应该找回多少钱
"""

# price_unit = float(input('输入商品单价：'))
# amounts = int(input('输入购买商品的数量:'))
# money = int(input('输入你支付了多少钱：'))
#
# Change = money - amounts * price_unit
# print('找回%.2f元' % Change)

"""
获取分钟、小时、天
计算总秒数
"""
# minutes = int(input('输入分钟:'))
# hours = int(input('输入小时：'))
# days = int(input('输入天数：'))
#
# seconds = minutes * 60 + hours * 3600 + days * 86400
# print('总共是%d秒' % seconds)

"""
一斤10两
输入两,计算几斤几两
"""
# weights = int(input('输入几两：'))
# result1 = weights // 10
# result2 = weights % 10
# print("%d两是%d斤%d两" % (weights, result1, result2))

"""
录入距离、时间、初速度
计算加速度  x = v0 + 1/2 * a * (t^2)
"""
# distance = float(input('输入距离：'))
# speed0 = float(input('输入初速度：'))
# time = float(input('输入时间：'))
#
# Acceleration = (distance - speed0) * 2 / (time ** 2)
# print('加速度为%.2f' % Acceleration)

"""
录入四位整数
计算每位数相加的和
"""
# number = int(input('输入一个四位整数：'))
# number1 = number % 10
# number2 = number % 100 // 10
# number3 = number // 100 % 10
# number4 = number // 1000
# sum = number1 + number2 + number3 + number4
#
# print('%d+%d+%d+%d=%d' % (number4, number3, number2, number1, sum))
# ==========================================================================
# number_str = input('输入一个四位整数：')
# result = 0
# for i in number_str:
#     result += int(i)
# print(result)

# sex = input('输入性别：')
# if sex == "男":
#     print("你好，先生！")
# elif sex == "女":
#     print("你好，女士！")
# else:
#     print("输入有误！")
