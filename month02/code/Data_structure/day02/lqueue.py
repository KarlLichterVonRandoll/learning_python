"""
    队列： 链式存储
    入队、出队、队空、队满
"""


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LQueue:
    def __init__(self, length):
        self.length = length
        self.head = Node()

    def len(self):
        p = self.head
        count = 0
        while p.next is not None:
            p = p.next
            count += 1
        return count

    def is_empty(self):
        return self.head.next is None

    def is_full(self):
        return self.len() == self.length

    def enqueue(self, item):
        """
            使用遍历的方式入队
        """
        if self.is_full():
            raise Exception("队满!")
        node = Node(item)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node

    def dequeue(self):
        if self.is_empty():
            raise Exception("队空!")
        item = self.head.next.item
        self.head.next = self.head.next.next
        return item


if __name__ == "__main__":
    lq = LQueue(5)
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)
    lq.enqueue(5)
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    lq.dequeue()
    print(lq.len())
