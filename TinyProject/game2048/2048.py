import curses
from random import randrange, choice
from collections import defaultdict

# 定义有效输入 上、下、左、右、重置、退出
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

letter_codes = [ord(ch) for ch in "WASDRQwasdqr"]

actions_dict = dict(zip(letter_codes, actions * 2))


def main(stdscr):
    def init():
        # 重置游戏
        return "Game"

    def not_game(state):
        # 画出 GameOver 或者 Win 的界面
        # 读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda: state)  # 默认为当前状态
        responses['Restart'], responses['Exit'] = "Init", 'Exit'  # 对应不同行为转换到不同状态
        return responses[action]

    def game():
        # 画出当前棋盘状态
        # 读取用户输入得到 action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'


def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


# 矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]


# 矩阵逆转
def invert(field):
    return [row[::-1] for row in field]


class GameField:
    def __init__(self, height=4, width=4, win=2048):
        self.height = height  # 高
        self.width = width  # 宽
        self.win_value = 2048  # 过关分数
        self.score = 0  # 当前分数
        self.highscore = 0  # 最高分
        self.reset()  # 棋盘重置

    # 随机生成 2 或 4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    # 重置棋盘
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()


    # 一行向左合并
    def move_row_left(row):
        # 将零散的非零单元挤到一块
        def tighten(row):
            new_row = [i for i in row if i != 0]
            new_row += [0 for i in range(len(row) - len(new_row))]
            return new_row

        # 对邻近元素进行合并
        def merge(self, row):
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    new_row.append(2 * row[i])
                    self.score += 2 * row[i]
                    pair = False
                else:
                    if i + 1 < len(row) and row[i] == row[i + 1]:
                        pair = True
                        new_row.append(0)
                    else:
                        new_row.append(row[i])
            assert len(new_row) == len(row)
            return new_row
            # 先挤到一块再合并再挤到一块

        return tighten(merge(tighten(row)))
