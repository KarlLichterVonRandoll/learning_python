"""
    二分查找
"""


def binary_search01(x, list_):
    if len(list_) == 0:
        raise Exception("No Found")
    mid = len(list_) // 2
    if x == list_[mid]:
        return mid
    elif x < list_[mid]:
        return binary_search01(x, list_[0:mid])
    elif x > list_[mid]:
        return mid + 1 + binary_search01(x, list_[mid + 1:])


def binary_search02(x, list_):
    low, high = 0, len(list_)-1

    while low <= high:
        mid = (low+high) // 2
        if x < list_[mid]:
            high = mid-1
        elif x > list_[mid]:
            low = mid + 1
        else:
            return mid
    else:
        return "No found"


l = [1, 2, 3, 4, 5, 6, 9, 60, 666]
print("key index:", binary_search02(7, l))
