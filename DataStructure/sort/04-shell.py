"""
    希尔排序：插入排序的一种，也称缩小增量排序，是直接插入排序的一种改进版
    基本思想： 希尔排序会记录按下标的一定增量分组，对每组使用直接插入排序；
             随着增量的减少，每组包含的关键词越来越多，当增量减到 1 时，
             整个文件恰被分成一组，算法便终止。
"""
import random
import time


def shell_sort(list_):
    # 设定步长
    step = len(list_) // 2
    while step > 0:
        for i in range(step, len(list_)):
            # 将当前值与指定步长之前的值进行比较，符合条件则交换位置
            while i >= step and list_[i - step] > list_[i]:
                list_[i], list_[i - step] = list_[i - step], list_[i]
                i -= step  # 将当前值指定步长前的值作为下次循环的当前值，再与其指定步长之前的值进行比较
        print(list_)
        step = step // 2  # 步长改为之前的二分之一


# list01 = [random.randint(1, 999) for i in range(10000)]
# list02 = list01.copy()
# print(list01[:50])
#
# start01 = time.clock()
# shell_sort(list01)
# print("希尔排序结果:", time.clock() - start01)
# print(list01[:50])
#
# start02 = time.clock()
# list02.sort()
# print("sort() 函数排序结果:", time.clock() - start02)
# print(list02[:50])
#
# print(list01 == list02)

list03 = [3, 4, 9, 0, 2, 6, 7, 1, 2, 8, 9, 1, 1]
shell_sort(list03)
print(list03)
