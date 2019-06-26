import random


class Direction:
    """
        方向数据模型
        添加一个容易识别的标签
    """
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"


class MapModel:
    def __init__(self, rank):
        self.__rank = rank

    def generate_map(self):
        map01 = []
        n = 4
        for i in range(self.__rank):
            list01 = []
            for j in range(self.__rank):
                number = random.randint(1, 10)
                if number == 1:
                    list01.append(8)
                elif number < 3:
                    list01.append(4)
                else:
                    list01.append(random.choice([0, 2]))
            map01.append(list01)
        return map01
