"""
    选择排序
    时间复杂度： O(n^2)
    额外空间：   O(1)
    特点：    适合数据量较少的情况
    基本思想： 第一次，在待排序的数据 r(1)~r(n) 中选出最小的，将它与 r(1) 交换；
             第二次，在待排序的数据 r(2)~r(n) 中选出最小的，将它与 r(2) 交换；
             以此类推...
             第 i 次，在待排序的数据 r(i)~r(n) 中选出最小的，将它与 r(i) 交换
"""
import random
import time


def select_sort(list_):
    for i in range(len(list_) - 1):
        min_index = i  # 已排序好的序列的最后一个元素的下标 i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:  # 找出未排序的序列中最小值的下标 min_index
                min_index = j
        if min_index != i:  # 对应的元素值交换
            list_[i], list_[min_index] = list_[min_index], list_[i]


list01 = [random.randint(1, 999) for i in range(10000)]
list02 = list01.copy()
print(list01[:50])

start01 = time.clock()
select_sort(list01)
print("选择排序结果:", time.clock() - start01)
print(list01[:50])

start02 = time.clock()
list02.sort()
print("sort() 函数排序结果:", time.clock() - start02)
print(list02[:50])

