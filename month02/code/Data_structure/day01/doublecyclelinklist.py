"""
    双向循环链表
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None


class DoubleCycleLinkList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head
        self.head.pre = self.head

    def init_list(self, list_):
        p = self.head
        for item in list_:
            self.append(item)

    def append(self, item):
        p = self.head
        node = Node(item)
        while p.next is not self.head:
            p = p.next
        p.next = node
        node.pre = p
        node.next = self.head
        self.head.pre = node

    def travel(self):
        p = self.head.next
        while p is not self.head:
            print(p.val)
            p = p.next

    # 判断列表是否为空
    def is_empty(self):
        return self.head.next is self.head

    # 计算列表长度
    def len(self):
        p = self.head
        count = 0
        while p.next is not self.head:
            count += 1
            p = p.next
        return count
