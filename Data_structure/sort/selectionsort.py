"""
    选择排序
    最优时间复杂度 O(n2)
    最坏时间复杂度 O(n2)
    1. 首先在未排序中找到最小(大)元素，存放到排序序列的起始位置
    2. 再从剩余未排序元素中继续寻找最小(大)元素，然后放到已排序序列的末尾，以此类推
    3. 重复第 2 步，直到所有元素均排序完毕
"""


def selection_sort(alist):
    for i in range(len(alist)):
        # 记录最小位置
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选出的数据不在正确位置，则进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == "__main__":
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(alist)
    print(alist)
