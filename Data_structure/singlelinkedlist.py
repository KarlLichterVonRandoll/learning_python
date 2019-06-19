"""
    单向列表操作类
    单位元素的定义： 必须包含至少两个内容, 数据和指针
    遍历算法：采取循环，只要下一个元素不为空就继续
"""


class SingleNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    def __init__(self):
        self._head = None

    # 判断列表是否为空
    def is_empty(self):
        return self._head is None

    # 计算列表长度
    def length(self):
        cur = self._head

        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    # 遍历
    def travel(self):
        cur = self._head

        while cur:
            print(cur.item)
            cur = cur.next

    # 开头添加
    def add_first(self, item):
        node = SingleNode(item)

        node.next = self._head
        self._head = node

    # 末尾添加
    def append(self, item):
        node = SingleNode(item)

        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    # 指定位置插入
    def insert(self, pos, item):
        if pos <= 0:
            self.add_first(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    # 删除元素
    def remove(self, item):
        cur = self._head
        pre = None

        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    # 搜索元素
    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    s01 = SingleLinkList()

    s01.add_first(10)
    s01.add_first(20)

    s01.append(30)
    s01.insert(2, 4)

    print("Length of s01 is {}".format(s01.length()))

    s01.travel()

    print(s01.search(30))
    print(s01.search(32))

    s01.remove(20)
    print("Length of s01 is {}".format(s01.length()))
    s01.travel()

