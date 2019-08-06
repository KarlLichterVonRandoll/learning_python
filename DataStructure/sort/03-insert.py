"""
    插入排序
    时间复杂度: O(n^2)
    额外空间:  O(1)
    特点：    适用于大部分已排序好的情况
    基本思想： 将当前需要排序的元素r[i]，跟已经排序好的序列的最后一个元素r[i-1]比较;
             如果满足条件则继续执行后面的程序，否则循环到下一个要排序的元素；
             缓存当前要排序的元素的值，以便找到正确的位置进行插入；
             排序的元素和已经排序好的元素比较， 比他大的向后移动（升续）
             要排序的元素，插入到正确的位置
"""
import random
import time


def insert_sort1(list_):
    for i in range(1, len(list_)):
        if list_[i] < list_[i - 1]:  # 当前要排序的元素比前面的小
            index = i  # 保存当前元素的下标，用来记录排序元素需要插入的位置
            temp = list_[i]  # 保存当前元素的值
            while index > 0 and list_[index - 1] > temp:  # 找到正确的插入位置
                list_[index] = list_[index - 1]  # 记录右移
                index -= 1
            list_[index] = temp


def insert_sort2(list_):
    pre, value = 0, list_[0]  # 记录上一个插入值的位置和值,初始为序列的第一个值

    for i in range(1, len(list_)):
        temp = list_[i]
        start = i - 1
        # 根据上一个插入的值，定位开始遍历的位置
        if temp < value:
            start = pre
            for j in range(i - 1, start - 1, -1):
                list_[j + 1] = list_[j]
        for k in range(start, -1, -1):
            if temp < list_[k]:
                list_[k + 1] = list_[k]
                if k == 0:
                    list_[k] = temp
            else:
                list_[k + 1] = temp
                value = temp
                pre = k + 1
                break


# list01 = [random.randint(1, 999) for i in range(10000)]
# list02 = list01.copy()
# print(list01[:50])
#
# start01 = time.clock()
# insert_sort1(list01)
# print("选择排序结果:", time.clock() - start01)
# print(list01[:50])
#
# start02 = time.clock()
# insert_sort2(list02)
# print("选择排序结果:", time.clock() - start02)
# print(list02[:50])
#
# print(list01 == list02)
#
#
# start02 = time.clock()
# list02.sort()
# print("sort() 函数排序结果:", time.clock() - start02)
# print(list02[:50])

list03 = [3, 5, 1, 5, 10, 2, 9, 8, 7, 1]
insert_sort2(list03)
print(list03)
