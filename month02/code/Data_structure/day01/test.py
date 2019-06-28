from linklist import LinkList
from cyclelinklist import CycleLinkedList
from doublecyclelinklist import DoubleCycleLinkList
import time

l1 = LinkList()
l2 = LinkList()
l1.init_list([1, 3, 5, 7, 9])
l2.init_list([2, 4, 6, 8, 10])
l1.merge_list(l2)

l1.show()
