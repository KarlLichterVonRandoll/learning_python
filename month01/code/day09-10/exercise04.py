# 在二维列表中获取指定位置、指定方向、指定数量的元素
class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:

    @staticmethod
    def get_elements(target, vector_pos, vector_dir, count):
        list01 = []
        for i in range(count):
            vector_pos.x += vector_dir.x
            vector_pos.y += vector_dir.y
            list01.append(target[vector_pos.x][vector_pos.y])
        return list01


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]
# 在二维列表中，获取13位置，向左，3个元素
re01 = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
print(re01)
# 在二维列表中，获取22位置，向上，2个元素
re02 = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
print(re02)
# 在二维列表中，获取03位置，向下，2个元素
re03 = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
print(re03)
