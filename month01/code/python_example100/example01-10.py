"""
    练习 1：有 1,2,3,4 四个数字，能组成多少个互不相同且无重复的三位数
"""
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and j != k and i != k:
#                 print(i, j, k)


"""
    练习 2：企业发放的奖金根据利润提成。
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，
    高于100万元时，超过100万元的部分按1%提成，
    从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。       
"""
# profit = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# money_reward = 0
# for idx in range(0, 6):
#     if profit > arr[idx]:
#         money_reward += (profit - arr[idx]) * rate[idx]
#         profit = arr[idx]
# print(money_reward)


"""
    练习 3: 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
    1.则：x + 100 = n**2, x + 100 + 168 = m**2
    2.(m + n) * (m -n) = 168  ==>  i * j = 168  则 i和j 至少有一个是偶数
    3.再由 m = (i+j) / 2  n = (i-j) / 2  又因为 m和n 必须都是整数，
      得到 i和j 要么都是偶数 要么都是奇数
    4.由 2,3 推导可知 i和j 一定都是偶数
"""

# for i in range(1, 169//2):
#     if 168 % i == 0:
#         j = 168 / i
#         if i < j and i % 2 == 0 and j % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = m ** 2 - 268
#             print(x)


"""
    练习 4:输入某年某月某日，判断这一天是这一年的第几天？
    程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
    特殊情况，闰年且输入月份大于2时需考虑多加一天.
"""
# month_tuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# year = int(input("输入年份："))
# month = int(input("输入月份(1-12)："))
# day = int(input("输入日期(1-31)："))
#
# if (year % 4 == 0 and year % 100 != 100 or year % 400 == 0) and month > 2:
#     print("这是一年中的第%d天" % ((sum(month_tuple[:month - 1]) + day) + 1))
# else:
#     print("这是一年中的第%d天" % (sum(month_tuple[:month - 1]) + day))


"""
    练习 5:输入三个整数x,y,z，请把这三个数由小到大输出。
    程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
    然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小
"""
# 方法一
# x = int(input("输入第一个数："))
# y = int(input("输入第二个数："))
# z = int(input("输入第三个数："))
# if x > y:
#     x, y = y, x
# if x > z:
#     x, z = z, x
# if y > z:
#     y, z = z, y
# print(x,y,z)

# 方法二
# list01 = []
# for i in range(3):
#     number = int(input("输入数字："))
#     list01.append(number)
# list01.sort()
# print(list01)


"""
    练习 6： 输出斐波那契数列(前50个)
"""
# list02 = [1,1]
# for i in range(50):
#     list02.append(list02[i] + list02[i+1])
# print(list02)


"""
    练习 7： 将一个列表的数据复制到另一个列表中
"""
# list01 = [1,2,3,4]
# list02 = list01[:]
# print(list02)


"""
    练习 8：
    输出 9*9 乘法口诀表。
    程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
# for i in range(1,10):
#     for j in range(1, i+1):
#         print("%d*%d=%d "%(i,j,i*j),end="")
#     print()


"""
    练习 9：暂停一秒输出。
    程序分析：使用 time 模块的 sleep() 函数。
"""
# import time
#
# for i in range(5):
#     print(i)
#     time.sleep(1)


"""
    练习 10： 暂停一秒输出，并格式化当前时间。
"""
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 暂停一秒
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
