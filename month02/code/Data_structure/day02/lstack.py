"""
    栈： 链式存储
    1. 源于链表结构
    2. 入栈、出栈、栈空、栈顶元素
    3. 链表开头作为栈顶 （不用每次遍历)
"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LStack:
    def __init__(self):
        self._top = None

    def push(self, item):
        self._top = Node(item, self._top)

    def is_empty(self):
        return self._top is None

    def top(self):
        if self.is_empty():
            raise Exception("栈为空")
        return self._top.item

    def pop(self):
        if self.is_empty():
            raise Exception("栈为空")
        value = self._top.item
        self._top = self._top.next
        return value


if __name__ == "__main__":
    lstack = LStack()
    lstack.push(1)
    lstack.push(2)
    lstack.push(3)
    print(lstack.top())
    lstack.pop()
    lstack.pop()
    lstack.pop()
    print(lstack.top())
