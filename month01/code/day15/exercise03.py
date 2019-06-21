"""
    敌人类：
    攻击力 范围在 0-100
    否则跑出异常信息，消息、错误航、攻击力、错误编号
"""


class AtkError(Exception):
    def __init__(self, message, code_line, atk, id):
        super().__init__("gg")
        self.message = message
        self.code_line = code_line
        self.atk = atk
        self.id = id


class Enemy:
    def __init__(self, atk):
        try:
            self.atk = atk
        except AtkError as e:
            print(e)
            print("error")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError("超出范围了", 18, value, 404)

try:
    enemy = Enemy(120)
except AtkError as e:
    print(e)
    print("重新输入")


