"""
    天龙八部技能系统类
"""


# 职业类
class Profession:
    def __init__(self, name):
        self.name = name
        self.__manager = SkillManager()

    def add_skill(self, skill):
        self.__manager.add_skill(skill)

    def attack(self, name):
        for item in self.__manager.get_skill_list():
            if item.name == name:
                print("发动", name)
                item.release_skills()


# 技能管理类
class SkillManager:
    def __init__(self):
        self.__Skill_list = []

    def add_skill(self, skill):
        self.__Skill_list.append(skill)

    def get_skill_list(self):
        return self.__Skill_list


class Skill:
    def __init__(self, name, category, mp, cd):
        self.name = name
        self.category = category
        self.mp = mp
        self.cd = cd

    def release_skills(self):
        pass


class ShaolinGeneralAttack(Skill):
    def __init__(self, name, category, mp, cd):
        super().__init__(name, category, mp, cd)

    def release_skills(self):
        print("攻击单个近身敌人，对目标每秒造成100%外功攻击伤害。自动连续攻击")


profession01 = Profession("少林")
skill01 = ShaolinGeneralAttack("少林普攻", "瞬发技能", 0, 0)
skill02 = ShaolinGeneralAttack("少林普攻", "瞬发技能", 0, 0)
skill03 = ShaolinGeneralAttack("少林普攻", "瞬发技能", 0, 0)
profession01.add_skill(skill01)
profession01.attack("少林普攻")
