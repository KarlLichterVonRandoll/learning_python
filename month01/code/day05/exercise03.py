"""
    1.计算列表中的最小值 不使用 min
"""
# list01 = [3, 4, 55, 0, -1, 6, 9, 44, -6, 88]
# min_value = list01[0]
# for i in range(1, len(list01)):
#     if list01[i] < min:
#         min_value = list01[i]
# print(min_value)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
彩票　双色球： 
红球:6个，1 -- 33 之间的整数   不能重复
蓝球:1个，1 -- 16 之间的整数
(1) 随机产生一注彩票[6个红球１个蓝球].
(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："
"""
import random

# 生成彩票号码
lottery_number = []
# 产生红球号码
while len(lottery_number) < 6:
    number = random.randint(1, 33)
    # 如果随机数不存在则存储
    if number not in lottery_number:
        lottery_number.append(number)
    # 产生蓝球号码
lottery_number.append(random.randint(1, 16))

# 购买彩票，选择号码
your_number = []
# 选择红球号码
while len(your_number) < 6:
    number = int(input("输入第%d个红球号码(1-33)" % (len(your_number) + 1)))
    if number not in your_number and 1 <= number <= 33:
        your_number.append(number)
    else:
        print("号码重复或不在范围内！")
# 选择蓝球号码
while True:
    blue_number = int(input("输入蓝球号码(1-16)："))
    if 1 <= blue_number <= 16:
        your_number.append(blue_number)
        break
    print("输入有误！重新输入")

print("中奖号码是：", lottery_number)
print("你的号码是：", your_number)
