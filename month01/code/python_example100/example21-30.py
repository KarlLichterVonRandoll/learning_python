"""
    练习 21：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
    还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
    以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
    求第一天共摘了多少。
    程序分析：采取逆向思维的方法，从后往前推断。
"""
# sum_peach = 1
# for i in range(9):
#     sum_peach = (sum_peach + 1) * 2
# print(sum_peach)


"""
    练习 22：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
    已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
    请编程序找出三队赛手的名单。
"""
# for i in "xyz":
#     for j in "xyz":
#         if i != j:
#             for k in "xyz":
#                 if k != i and k != j:
#                     if i != "x" and k != "x" and k != "z":
#                         print("a-->%s,b-->%s,c-->%s" % (i, j, k))


"""
    练习 23：打印出如下图案（菱形）:
              *
             ***
            *****
           *******
            *****
             ***
              *
"""
# for i in range(1, 5):
#     print(" " * (5 - i), end="")
#     print("*" * (2 * i - 1))
#
# for i in range(1, 4):
#     print(" " * (i + 1), end="")
#     print("*" * ((4 - i) * 2 - 1))


"""
    练习 24 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...
    求出这个数列的前20项之和。
"""
# a = 1
# b = 2
# s = 0
# for i in range(1,3):
#     s += b / a
#     t = a
#     a = b
#     b = t + b
#
# print(s)

"""
    练习 25 求1+2!+3!+...+20!的和
"""

sum = 0

t = 1
for i in range(1, 21):
    t *= i
    sum += t
print(sum)
