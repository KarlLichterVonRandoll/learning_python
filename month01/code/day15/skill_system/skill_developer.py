"""
    skill_developer
"""


skill_list = ["伤害生命", "眩晕"]


def func():
    print("func -- skill_developer")


class Developer:
    @staticmethod
    def func():
        print("class_func -- skill_developer")

from skill_system import skill_manager

