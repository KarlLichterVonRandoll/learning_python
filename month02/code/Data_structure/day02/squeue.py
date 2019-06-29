"""
    队列： 顺序存储
    入队、出队、队空、队满
"""


class SQueue:
    def __init__(self, length):
        self.__list = []
        self.length = length

    def is_empty(self):
        return self.__list == []

    def is_full(self):
        return len(self.__list) == self.length

    def len(self):
        return len(self.__list)

    def enqueue(self, item):
        if self.is_full():
            raise Exception("队满！")
        self.__list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("队空！")
        return self.__list.pop(0)


if __name__ == "__main__":
    squeue = SQueue(5)
    squeue.enqueue('a')
    print(squeue.len())
    squeue.enqueue('b')
    print(squeue.len())
    squeue.enqueue('c')
    print(squeue.len())
    squeue.enqueue('d')
    print(squeue.len())
    squeue.enqueue('e')
    print(squeue.len())
    print(squeue.dequeue())
    print(squeue.dequeue())
    print(squeue.dequeue())
    print(squeue.len())
    squeue.enqueue('f')
