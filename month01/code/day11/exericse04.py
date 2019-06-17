"""
    3. 请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。
"""

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     def get_money(self, value):
#         print("%s 上班 挣了 %d" % (self.__name, value))
#
#     def teach(self, person, value):
#         print("%s 教 %s %s" % (self.__name, person.name, value))
#
#
# person01 = Person("张无忌")
# person02 = Person("赵敏")
#
# person01.teach(person02, "九阳神功")
# person02.teach(person01, "化妆")
# person01.get_money(10000)
# person02.get_money(6000)


"""
    4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
"""


class Player:
    __slots__ = ("__atk", "__hp", "point")

    def __init__(self, atk, hp, point=0):
        self.atk = atk
        self.hp = hp
        self.point = point

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def injured(self, value):
        self.__hp -= value
        if self.__hp > 0:
            print("玩家受伤,剩余血量 %d" % self.__hp)
        else:
            Player.__death()

    @staticmethod
    def __death():
        print("玩家死亡")

    def attack(self, enemy):
        print("玩家攻击敌人", end=" ")
        enemy.injured(self.atk)
        if enemy.hp <= 0:
            self.point += 10
            print("玩家得分%d" % self.point)
        else:
            print("玩家得分%d" % self.point)


class Enemy:
    __slots__ = ("__atk", "__hp")

    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def injured(self, value):
        self.__hp -= value
        if self.__hp > 0:
            print("敌人受伤,剩余血量 %d" % self.__hp)
        else:
            Enemy.__death()

    @staticmethod
    def __death():
        print("敌人死亡, 掉装备, 玩家加分")

    def attack(self, player):
        print("敌人攻击玩家", end=" ")
        player.injured(self.atk)


p01 = Player(50, 100)
e01 = Enemy(30, 100)
p01.attack(e01)
p01.attack(e01)
e01.attack(p01)
e01.attack(p01)
