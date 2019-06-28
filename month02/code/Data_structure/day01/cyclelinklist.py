"""
    循环链表
"""


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class CycleLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head

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

    # 遍历
    def travel(self):
        if self.is_empty():
            return
        p = self.head.next
        while p is not self.head:
            print(p.item)
            p = p.next

    # 初始化循环链表
    def init_list(self, _list):
        for item in _list:
            self.append(item)

    # 开头添加
    def head_add(self, item):
        node = Node(item)
        # 如果链表为空, 将node定义为头节点, node的next指向自己
        if self.is_empty():
            self.head.next = node
            node.next = self.head
        # 如果链表不为空, 将node的next指向头结点, 将链表最后一个节点的next指向node
        else:
            node.next = self.head.next
            self.head.next = node

    # 末尾添加
    def append(self, item):
        node = Node(item)
        p = self.head
        while p.next is not self.head:
            p = p.next
        p.next = node
        node.next = self.head

    # 指定位置插入
    def insert(self, pos, item):
        node = Node(item)
        if pos <= 0:
            self.head_add(item)
        elif pos > self.len() - 1:
            self.append(item)
        else:
            i = 0
            p = self.head
            while i < pos:
                i += 1
                p = p.next
            node.next = p.next
            p.next = node

    # 删除元素
    def remove(self, item):
        if self.is_empty():
            return
        p = self.head.next
        while p.next is not self.head and p.next.item != item:
            p = p.next
        if p.next is self.head:
            print("no this value")
            return
        else:
            p.next = p.next.next
