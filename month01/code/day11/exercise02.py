"""
    封装设计思想
        需求：老张开车去东北
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def goto(self, str_pos, type):
        print(self.__name, "去", str_pos)
        type.run(str_pos)


class Car:

    def run(self, str_pos):
        print("行驶到:", str_pos)


lz = Person("老张")
car = Car()

lz.goto("东北", car)
