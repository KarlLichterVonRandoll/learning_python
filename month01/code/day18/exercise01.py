"""
    获取元组中长度最大的列表
"""

tuple01 = ([1, 1], [2], [3, 3, 3])

re01 = max(tuple01, key=lambda x: len(x))
print(re01)


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

"""
    获取所有敌人的姓名、血量和攻击力
"""
re02 = list(map(lambda x: (x.name, x.hp, x.atk), list_enemy))
print(re02)

"""
    获取攻击力大于 100 的所有活人
"""
re03 = list(filter(lambda x: x.hp != 0, list_enemy))
for item in re03:
    print(item)

"""
    根据防御力对敌人列表进行降序排列
"""
list_enemy = sorted(list_enemy, key=lambda x: x.defense, reverse=True)
for item in list_enemy:
    print(item)
