"""
    skill_manager
"""


manager_list = ["manager01", "manager02"]


def func():
    print("func -- skill_manager")


class Manager:
    @staticmethod
    def func():
        print("class_func -- skill_manager")

from common import double_list_helper

manager = Manager()
manager.func()

