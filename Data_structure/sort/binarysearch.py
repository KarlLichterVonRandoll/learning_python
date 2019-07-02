"""
    二分查找
"""


def binary_search(x, list_):
    if len(list_) == 0:
        return False
    mid = len(list_) // 2
    if x == list_[mid]:
        return True
    elif x < list_[mid]:
        return binary_search(x, list_[0:mid])
    else:
        return binary_search(x, list_[mid + 1:])


print(binary_search(3, [1, 2, 3, 4, 5, 6]))
