"""
    天龙八部技能系统
"""


class SkillDeveloper:
    """
        技能释放器
    """

    def __init__(self, name):
        # 技能名字
        self.name = name
        # 加载配置文件
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_obj = self.__create_effect_obj()

    # 加载配置文件
    def __load_config_file(self):
        return {"降龙十八掌": ['DamageEffect(200)', 'DizzinessEffect(6)'],
                "六脉神剑": ['DamageEffect(150)', 'DizzinessEffect(4)'],
                "北冥神功": ['DamageEffect(250)', 'DizzinessEffect(6)'],
                }

    # 创建效果对象
    def __create_effect_obj(self):
        # 根据名字创建效果对象
        list_effect_name = self.__dict_skill_config[self.name]
        # 效果对象列表
        list_effect_obj = []

        for item in list_effect_name:
            list_effect_obj.append(eval(item))

        return list_effect_obj

    # 执行效果
    def generate_skill(self):
        print(self.name + "释放")
        for item in self.__effect_obj:
            item.impact()


class SkillEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise Exception


class DizzinessEffect(SkillEffect):
    """
        眩晕  持续时间
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕%d秒" % self.time)


class LowerDefenseEffect(SkillEffect):
    """
        降低防御力  防御力数值+持续时间
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低防御力%d,持续%d秒" % (self.value, self.time))


# 伤害生命
class DamageEffect(SkillEffect):
    """
        伤害生命  扣血数值
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


skill01 = SkillDeveloper("降龙十八掌")
skill01.generate_skill()
print("# # " * 10)
skill02 = SkillDeveloper("六脉神剑")
skill02.generate_skill()
print("# # " * 10)
skill03 = SkillDeveloper("北冥神功")
skill03.generate_skill()
