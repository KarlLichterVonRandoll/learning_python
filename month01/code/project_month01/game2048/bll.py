from model import *
import random


class GameCoreController:
    def __init__(self, map_list):
        self.__map = map_list

    @property
    def map(self):
        return self.__map

    @staticmethod
    def __zero_to_end(num_list):
        """
            零元素移动到末尾
        """
        # 从后向前，如果发现零元素，删除并在末尾追加 0
        for i in range(-1, -len(num_list) - 1, -1):
            if num_list[i] == 0:
                del num_list[i]
                num_list.append(0)

    def __merge(self, num_list):
        """
            合并
        """
        # 先将中间的零元素一直末尾，在合并相同元素
        self.__zero_to_end(num_list)
        for i in range(len(num_list) - 1):
            if num_list[i] == num_list[i + 1]:
                # 将后一个累加前一个之上
                num_list[i] *= 2
                del num_list[i + 1]
                num_list.append(0)

    def __move_left(self):
        """
            左移
        """
        for i in range(len(self.map)):
            # 合并
            self.__merge(self.map[i])

    def __move_right(self):
        """
            右移
        """
        for i in range(len(self.map)):
            # 从右向左取出数据形成新列表
            self.map[i] = self.map[i][::-1]
            # 合并
            self.__merge(self.map[i])
            # 从右向左接受合并后的数据
            self.map[i] = self.map[i][::-1]

    def __square_matrix_transpose(self):
        """
            矩阵转置
        """
        for i in range(len(self.map)):
            for j in range(i + 1, len(self.map)):
                self.map[i][j], self.map[j][i] = self.map[j][i], self.map[i][j]

    def __move_up(self):
        """
            上移
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
            下移
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def move(self, direction):
        if direction == Direction.UP:
            self.__move_up()
        elif direction == Direction.DOWN:
            self.__move_down()
        elif direction == Direction.LEFT:
            self.__move_left()
        elif direction == Direction.RIGHT:
            self.__move_right()

    def generate_random(self):
        """
            生成随机值
        :return:
        """
        list_empty_pos = self.__get_empty_pos()
        if len(list_empty_pos) == 0:
            return
        row, column = random.choice(list_empty_pos)
        self.map[row][column] = 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_pos(self):
        list_empty_pos = []
        for row in range(len(self.map)):
            for column in range(len(self.map[row])):
                if self.map[row][column] == 0:
                    list_empty_pos.append((row, column))
        return list_empty_pos

    def is_game_over(self):
        if len(self.__get_empty_pos()) > 0:
            return False

        for row in self.map:
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    return False

        for column in range(len(self.map)):
            for row in range(len(self.map) - 1):
                if self.map[row][column] == self.map[row + 1][column]:
                    return False

        return True
