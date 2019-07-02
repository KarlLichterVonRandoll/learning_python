# def bubble_sort(list_):
#     for i in range(len(list_) - 1, 0, -1):
#         for j in range(i):
#             if list_[j] > list_[j + 1]:
#                 list_[j], list_[j + 1] = list_[j + 1], list_[j]
#
#
# list01 = [5, 8, 3, 2, 1]
# bubble_sort(list01)
# print(list01)


def find(x, alist):
    mid = len(alist) // 2
    if x == alist[mid]:
        return mid
    elif x < alist[mid]:
        return find(x, alist[0:mid])
    else:
        return find(x, alist[mid+1:])

print(find(3,[1,2,3,4,5,6]))
