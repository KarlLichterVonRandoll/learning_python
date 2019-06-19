"""
    单向循环列表
    与单向列表不同, 循环列表中最后一个节点的next指向头结点
"""


class SingleNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCyLinkedList:
    def __init__(self):
        self._head = None

    # 判断列表是否为空
    def is_empty(self):
        return self._head is None

    # 计算列表长度
    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self._head

        while cur.next is not self._head:
            count += 1
            cur = cur.next
        return count

    # 遍历
    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)

        while cur.next is not self._head:
            cur = cur.next
            print(cur.item)

    # 开头添加
    def add_first(self, item):
        node = SingleNode(item)
        # 如果链表为空, 将node定义为头节点, node的next指向自己
        if self.is_empty():
            self._head = node
            node.next = self._head
        # 如果链表不为空, 将node的next指向头结点, 将链表最后一个节点的next指向node
        else:
            node.next = self._head
            cur = self._head
            while cur.next is not self._head:
                cur = cur.next
            cur.next = node
            self._head = node

    # 末尾添加
    def append(self, item):
        node = SingleNode(item)

        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next is not self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    # 指定位置插入
    def insert(self, pos, item):
        if pos <= 0:
            self.add_first(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self._head
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    # 删除元素
    def remove(self, item):
        if self.is_empty():
            return
        cur = self._head
        pre = None

        if cur.item == item:
            if cur.next is not self._head:
                while cur.next is not self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                self._head = None
        else:
            pre = self._head
            while cur.next is not self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next

    # 搜索元素
    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next is not self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    l1 = SingleCyLinkedList()

    l1.add_first(10)
    l1.add_first(20)

    l1.append(30)
    l1.insert(2, 4)
    l1.insert(4, 5)
    l1.insert(0, 6)

    print("Length of s01 is {}".format(l1.length()))

    l1.travel()

    print(l1.search(30))
    print(l1.search(32))

    l1.remove(20)
    print("Length of s01 is {}".format(l1.length()))
    l1.travel()

