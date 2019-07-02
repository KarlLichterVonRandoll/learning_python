"""
    快速排序
"""


def quick_sort(alist, start, end):
    # 递归退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左到右移动的游标
    low = start

    # high为序列右边的由右到左的游标
    high = end

    while low < high:
        # 如果low与high不重合，high指向的元素不必基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]
        print(alist)
        # 如果low与high不重合，low指向的元素不必基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]
        print(alist)

    alist[low] = mid
    print(alist)
    quick_sort(alist, start, low - 1)

    quick_sort(alist, low + 1, end)


if __name__ == "__main__":
    list01 = [54, 54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(list01, 0, len(list01)-1)
    print(list01)

