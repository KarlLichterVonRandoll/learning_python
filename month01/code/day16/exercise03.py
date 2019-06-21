"""
    将图形管理器的迭代器版本改成 yield 实现
"""


# 图形管理器
class GraphicsManager:
    def __init__(self):
        self.__Graphics = []

    def add_graphics(self, graphic):
        self.__Graphics.append(graphic)

    def __iter__(self):
        # number = 0
        # while number < len(self.__Graphics):
        #     yield self.__Graphics[number]
        #     number += 1

        # 执行过程：
        # 1.调用当前方法，不执行（内部创建迭代器对象）
        # 2.调用 __next__方法,才执行
        # 3.执行 yield 语句，暂时离开
        # 4.再次调用__next__方法,继续执行
        # 5.重复 3/4 步骤
        for item in self.__Graphics:
            yield item


# 图形类
class Graphic:
    pass


manager01 = GraphicsManager()
manager01.add_graphics(Graphic())
manager01.add_graphics(Graphic())
manager01.add_graphics(Graphic())
manager01.add_graphics(Graphic())

for item in manager01:
    print(item)
