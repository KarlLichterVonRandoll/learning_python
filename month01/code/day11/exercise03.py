"""
    小明在招商银行取钱
"""


class Person:
    def __init__(self, name, money):
        self.money = name
        self.money = money

    @property
    def money(self):
        return self.__name

    @money.setter
    def money(self, value):
        self.__name = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def draw_money(self, person, money):
        self.__money -= money
        person.money += money


xm = Person("小明", 1000)
bank = Bank("招商银行", 10000)
bank.draw_money(xm, 5000)

print(xm.money)
