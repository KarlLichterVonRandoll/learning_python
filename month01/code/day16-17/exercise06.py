from common.list_helper import *


class Enemy:
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    def __str__(self):
        return "%s atk %d defense %d hp %d" % (self.name, self.atk, self.defense, self.hp)


list_enemy = [
    Enemy("疯狂泰坦灭霸", 50, 30, 0),
    Enemy("青翼蝠王韦一笑", 8, 12, 8),
    Enemy("混元霹雳手成昆", 10, 10, 8),
    Enemy("金毛狮王谢逊", 10, 10, 10),
    Enemy("不败顽童古三通", 15, 10, 0),
    Enemy("铁胆神侯朱无视", 15, 10, 0),
]

re01 = ListHelper.find_single(list_enemy, lambda x: "灭霸" in x.name)
print(re01)

re02 = ListHelper.find_all(list_enemy, lambda x: x.atk > 10)
for item in re02:
    print(item)

re03 = ListHelper.find_all(list_enemy, lambda x: x.hp != 0)
for item in re03:
    print(item)

re04 = ListHelper.is_exists(list_enemy, lambda x: "海拉" in x.name)
print(re04)

re05 = ListHelper.is_exists(list_enemy, lambda x: x.atk < 5 or x.defense < 15)
print(re05)

re06 = ListHelper.get_sum(list_enemy, lambda x: x.hp + x.atk)
print(re06)

re07 = ListHelper.select(list_enemy, lambda x: (x.name, x.hp))
for item in re07:
    print(item, end=" ")

re07 = ListHelper.get_max(list_enemy, lambda x: x.hp)
print(re07)

ListHelper.order_by_up(list_enemy, lambda x: x.atk)
for item in list_enemy:
    print(item)

ListHelper.remove_enemy(list_enemy, lambda x: x.hp == 0)
for item in list_enemy:
    print(item)
