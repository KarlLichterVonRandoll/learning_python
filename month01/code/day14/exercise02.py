"""
    创建Enemy类对象，将对象打印在控制台
    克隆Enemy类对像
"""

# class Enemy:
#
#     def __init__(self, name, hp, atk, defense):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.defense = defense
#
#     def __str__(self):
#         return "%s 血量%d 攻击力%d 防御力%d" % (self.name, self.hp, self.atk, self.defense)
#
#     def __repr__(self):
#         return 'Enemy("%s",%d,%d,%d)' % (self.name, self.hp, self.atk, self.defense)
#
#
# enemy = Enemy("灭霸", 100, 80, 60)
# print(enemy)
#
# str01 = repr(enemy)
# print(str01)
# enemy02 = eval(str01)
# enemy02.name = "洛基"
# print(enemy02)


"""
    运算符重载
"""


class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "一唯向量的分量是 %d" % self.x

    def __add__(self, other):
        return Vector1(self.x + other)

    def __iadd__(self, other):
        self.x += other
        return self

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __mul__(self, other):
        return Vector1(self.x * other)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __rsub__(self, other):
        return Vector1(self.x - other)

    def __rmul__(self, other):
        return Vector1(self.x * other)


vec01 = Vector1(2)
print(vec01)
print(vec01 + 3)
print(vec01 - 4)
print(vec01 * 5)
print()
print(3 + vec01)
print(4 - vec01)
print(5 * vec01)

vec01 += 1
print(vec01)
