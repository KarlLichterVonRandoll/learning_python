"""
    插入排序
    - 对于未排序数据，在已排序序列中从后往前扫描
    - 找到相应位置插入。
    - 插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，
      为最新元素提供插入空间
"""


def insert_sort(alist):
    # 从第二个位置，索引为1的元素开始向前插入
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
            if alist[j] < alist[j-1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


if __name__ == "__main__":
    list01 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(list01)
    print(list01)
