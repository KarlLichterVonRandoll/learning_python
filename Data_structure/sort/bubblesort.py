"""
    冒泡排序
    最优时间复杂度 O(n)
    最坏时间复杂度 O(n2)
"""


def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


# def bubble_sort02(alist):
#     for i in range(len(alist)):
#         for j in range(i + 1, len(alist)):
#             if alist[j] > alist[i]:
#                 alist[j], alist[i] = alist[i], alist[j]


if __name__ == "__main__":
    list01 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(list01)
    print(list01)
