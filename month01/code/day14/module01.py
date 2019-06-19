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
        list02 = []
        for i in range(count):
            vector_pos.x += vector_dir.x
            vector_pos.y += vector_dir.y
            list02.append(target[vector_pos.x][vector_pos.y])
        return list02


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]

