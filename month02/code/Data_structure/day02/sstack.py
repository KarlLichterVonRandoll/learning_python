"""
    栈：顺序存储
    1. 列表即顺序存储，但功能多，不符合栈的模型特征
    2. 使用列表，将其封装，提供借口方法
"""


class SStack:
    def __init__(self):
        # 空列表作为栈的存储空间
        # 将栈的最后一个元素作为栈顶
        self.__items = []

    # 判断栈是否为空
    def is_empty(self):
        return self.__items == []

    # 进栈操作
    def push(self, item):
        self.__items.append(item)

    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise Exception("栈错误")
        return self.__items.pop()

    # 查看栈顶元素
    def top(self):
        return self.__items[-1]

    # 返回栈的长度
    def size(self):
        return len(self.__items)


if __name__ == "__main__":
    stack = SStack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.top())
