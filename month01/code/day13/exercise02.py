"""
    继承 -- 变量
"""


class Person:
    def __init__(self, name):
        self.name = name


# # 子类如果没有构造函数，则调用父类的构造函数
# class Student(Person):
#     pass


# 子类如果有构造函数，则必须先调用父类的构造函数
class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score


stu01 = Student("张无忌", 100)
print(stu01.name)

