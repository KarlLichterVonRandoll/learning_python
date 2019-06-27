from linklist import LinkList
from circularlinkedlist import CycleLinkedList
import time

l1 = CycleLinkedList()
l1.init_list([1, 2, 3, 4, 5])
l1.head_add(10)
l1.append(88)

l1.insert(6, 55)
l1.remove(88)
l1.travel()
