"""
    图形管理器记录多个图形
    迭代图形管理器对象
"""


# 图形迭代器
class GraphicsIterator:
    def __init__(self, manager):
        self.__list = manager
        self.index = 0

    def __next__(self):
        try:
            temp = self.__list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return temp


# 图形管理器
class GraphicsManager:
    def __init__(self):
        self.__Graphics = []

    def add_graphics(self, graphic):
        self.__Graphics.append(graphic)

    def __iter__(self):
        return GraphicsIterator(self.__Graphics)


# 图形类
class Graphic:
    pass


# manager01 = GraphicsManager()
# manager01.add_graphics(Graphic())
# manager01.add_graphics(Graphic())
# manager01.add_graphics(Graphic())
# manager01.add_graphics(Graphic())

# iterator = manager01.__iter__()

# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
#
# for item in manager01:
#     print(item)


"""
    定义 MyRange 类，实现下列功能
    for item in range(10):
        print(item)
"""


class MyRange:
    def __init__(self, number):
        self.number = number
        self.item = 0

    def __iter__(self):
        # return MyRangeIterator(self.number)
        # 使用 yield 将下列代码改成迭代器模式
        # 1.将 yield 以前的语句定义在 next 方法中
        # 2.将 yield 以后的数据作为方法的返回值
        number = 0
        while number < self.number:
            yield number
            number += 1


class MyRangeIterator:
    def __init__(self, end):
        self.__item = 0
        self.__end = end

    def __next__(self):
        if self.__item == self.__end:
            raise StopIteration
        temp = self.__item
        self.__item += 1
        return temp


# next一次，计算一次，返回一次
for item in MyRange(10):
    print(item)


