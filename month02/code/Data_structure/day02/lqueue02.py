"""
    队列： 链式存储
    入队、出队、队空、队满
"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LQueue:
    def __init__(self):
        """
            设置一个队尾
            初始化时，队头队尾指向同一节点
        """
        node = Node()
        self.head = node
        self.end = node

    def is_empty(self):
        return self.head == self.end

    def enqueue(self, item):
        """
            入队时，队头不变，队尾变
        """
        node = Node(item)
        self.end.next = node
        self.end = node

    def dequeue(self):
        """
            出队时，队头变，队尾不变
        :return:
        """
        if self.is_empty():
            raise Exception("队空")
        self.head = self.head.next
        return self.head.item


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)

    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())




