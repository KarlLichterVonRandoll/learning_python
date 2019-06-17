"""
    4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""


class Enemy:

    def __init__(self, name, blood, attack, defense):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.defense = defense

    def print_info(self):
        print("名字:%s,血量:%d,基础攻击力:%d,防御力:%d"
              % (self.name, self.blood, self.attack, self.defense))


enemy_list = [
    Enemy("青眼白龙", 100, 3000, 2500),
    Enemy("黑魔导", 0, 2500, 2000),
    Enemy("黑魔导女孩", 20, 2000, 1700),
    Enemy("真红眼黑龙", 0, 2400, 200),
    Enemy("欧西里斯的天空龙", 50, 9000, 9000),
    Enemy("奥贝里斯克的巨神兵", 50, 4000, 4000),
    Enemy("太阳神的翼神龙", 50, 9999, 9999)
]


# 查找姓名是"灭霸"的敌人对象
def find_enemy(enemy_name):
    for item in enemy_list:
        if item.name == enemy_name:
            item.print_info()


# 查找所有死亡的敌人
def find_death():
    for item in enemy_list:
        if item.blood == 0:
            item.print_info()


# 计算所有敌人的平均攻击力
def calculate_average_attack():
    summation = 0
    for item in enemy_list:
        summation += item.attack
    return summation / len(enemy_list)


# 删除防御力小于10的敌人
def delete_enemy():
    for i in range(len(enemy_list) - 1, -1, -1):
        if enemy_list[i].defense < 10:
            del enemy_list[i]


# 将所有敌人攻击力增加50
def add_attack(num):
    for item in enemy_list:
        item.attack += num


# add_attack(50)
# for item in enemy_list:
#     item.print_info()

find_death()
