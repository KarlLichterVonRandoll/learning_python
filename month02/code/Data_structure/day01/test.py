from linklist import LinkList
from cyclelinklist import CycleLinkedList
from doublecyclelinklist import DoubleCycleLinkList
import time

l1 = LinkList()
l2 = LinkList()
l1.init_list([1, 3, 5, 7, 9])
l2.init_list([2, 4, 6, 8, 10])
# l1.merge_list(l2)
#
# l1.show()


def merge(l1, l2):
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.item < q.item:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q


merge(l1, l2)
l1.show()
l1 = [0,  2, 3,       7, 8]
l2 = [  1,     4, 5, 6]
