"""
    冒泡排序
    特点：   适合数据量较小的情况
    基本思想：比较相邻元素大小，将小的元素前移，大的后移，最小的元素经过几次移动，会最终浮到最前面
    时间复杂度：O(n^2)  n个数排序需要进行n-1趟排序，第i趟排序
    额外空间： O(1)
"""
import random
import time


# def bubble_sort0(list_):
#     """
#         冒泡排序的初级版本
#         缺点：在排序好前面的数字后，对其余数字的排序没有多大帮助
#     """
#     for i in range(len(list_) - 1):
#         for j in range(i + 1, len(list_)):
#             if list_[i] > list_[j]:
#                 list_[i], list_[j] = list_[j], list_[i]


# 小数上浮
def bubble_sort1(list_):
    for i in range(len(list_)-1, -1, -1):
        for j in range(0, i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


# 优化
def bubble_sort2(list_):
    flag = True
    for i in range(len(list_)-1, -1, -1):
        if not flag:
            break
        else:
            flag = False
            for j in range(0, i):
                if list_[j] > list_[j + 1]:
                    list_[j], list_[j + 1] = list_[j + 1], list_[j]
                    flag = True


# list01 = [random.randint(1, 999) for i in range(10000)]
list01 = [2, 1] + [i for i in range(3, 9998)]
list02 = list01.copy()
print(list01[:50])

start01 = time.clock()
bubble_sort1(list01)
print("冒泡排序1.0结果:", time.clock() - start01)
print(list01[-50:])

start02 = time.clock()
bubble_sort2(list02)
print("冒泡排序2.0结果:", time.clock() - start02)
print(list02[-50:])

print(list01 == list02)

# start02 = time.clock()
# list02.sort()
# print("sort() 函数排序结果:", time.clock() - start02)
# print(list02[:50])

