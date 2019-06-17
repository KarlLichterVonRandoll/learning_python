"""
    练习 11：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
    小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""
# f1 = 1
# f2 = 1
# for i in range(1, 22):
#     print('%12ld %12ld' % (f1, f2))
#     if (i % 3) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 + f2


"""
    练习 12： 判断101-200之间有多少个素数，并输出所有素数。
    程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
    如果能被整除，则表明此数不是素数，反之是素数。
"""
# import math
# list01 = []
# for num in range(101, 201):
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             break
#     else:
#         list01.append(num)
#
# print(list01)
# print(len(list01))


"""
    练习 13：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
    程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位
"""
# for n in range(100, 1000):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)


"""
    练习 14: 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
    (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
    (2)如果n > k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
    (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
# import math
#
# list_number = []
#
# number = int(input("输入一个整数："))
# number01 = number
# while number != 1:
#     for i in range(2, number + 1):
#         if number % i == 0:
#             list_number.append(str(i))
#             number = number // i
#             break
#
# print(list_number)
# print("*".join(list_number) + "=" + str(number01))


"""
    练习 15： 利用条件运算符的嵌套来完成此题：
    学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
    程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""
# score = int(input('输入分数:'))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
#
# print('%d 属于 %s' % (score, grade))


"""
    练习 16：输出指定格式的日期。
"""
# import datetime
#
# # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
# print(datetime.date.today().strftime('%d/%m/%Y'))
# # 创建日期对象
# miyazakiBirthDate = datetime.date(1941, 1, 5)
# print(miyazakiBirthDate.strftime('%d/%m/%Y'))
# # 日期算术运算
# miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
# print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
# # 日期替换
# miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
# print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))


"""
    练习 17：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""
# str01 = input("输入一个字符串：")
# alpha, digit, space, others = 0,0,0,0
# for c in str01:
#     if c.isalpha():
#         alpha += 1
#     elif c.isdigit():
#         digit += 1
#     elif c == " ":
#         space += 1
#     else:
#         others += 1
# print("字母%d个，数字%d个，空格%d个，其他%d个" % (alpha, digit, space, others))


"""
    练习 18：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
    例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
    程序分析：关键是计算出每一项的值。 
"""
# a = int(input("输入 a:"))
# n = int(input("输入 n:"))
# sum = 0
# for i in range(1,n+1):
#     sum01 = 0
#     for j in range(i):
#         sum01 = sum01 + a * (10 ** j)
#     print(sum01)
#     sum += sum01
# print(sum)


"""
    练习 19:一个数如果恰好等于它的因子之和，这个数就称为"完数"。
    例如6=1＋2＋3.编程找出1000以内的所有完数
"""

# for num in range(1,1001):
#     list01 = []
#     for j in range(1, num):
#         if num % j == 0:
#             list01.append(j)
#
#     if sum(list01) == num:
#         print(list01, num)


"""
    练习 20：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
    再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
# height = 100
# distance = 100
# tims = 10
# for i in range(tims-1):
#     distance += height
#     height /= 2
# print(distance)
# print(height/2)
