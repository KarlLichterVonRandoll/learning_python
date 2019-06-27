"""
    link_list.py
    实现单链表的构建和功能操作
"""


class Node:
    """
        节点类： 包含数据和指向下一个节点的 next
    """

    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkList:
    """
        单链表类： 可以增删改查
    """

    def __init__(self):
        self.head = Node()

    # 初始化链表
    def init_list(self, list_):
        p = self.head
        for item in list_:
            node = Node(item)
            p.next = node
            p = p.next

    # 获取链表长度
    def len(self):
        p = self.head
        count = 0
        while p.next is not None:
            count += 1
            p = p.next
        return count

    # 遍历链表
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.item)
            p = p.next

    # 判断链表为空
    def is_empty(self):
        return self.head.next is None

    # 清空链表
    def clear(self):
        self.head.next = None

    # 头部添加元素
    def head_add(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

    # 末尾添加元素
    def append(self, value):
        p = self.head
        node = Node(value)
        while p.next is not None:
            p = p.next
        p.next = node

    # 指定位置插入
    def insert(self, index, value):
        p = self.head
        node = Node(value)
        # 如果超出位置最大范围就跳出循环
        for i in range(index):
            if p.next is None:
                break
            p = p.next

        node.next = p.next
        p.next = node

    # 删除指定元素
    def remove(self, value):
        p = self.head
        while p.next and p.next.item != value:
            p = p.next
        if p.next is None:
            print("value not in linklist")
            return
        else:
            p.next = p.next.next

    # 获取某个节点的值
    def index(self, index):
        if index < 0:
            raise IndexError("negative number error")
        p = self.head.next
        # 如果超出位置最大范围就跳出循环
        for i in range(index):
            if p.next is None:
                return "list index out of range"
            p = p.next

        return p.item

    def ordered_insert(self, value):
        p = self.head.next
        node = Node(value)
        if p.item >= value:
            node.next = p
            self.head.next = node
            return
        while p.next is not None:
            if p.next.item >= value:
                node.next = p.next
                p.next = node
                return
            p = p.next
        p.next = node



l = [0, 1, 2, 3, 4]
