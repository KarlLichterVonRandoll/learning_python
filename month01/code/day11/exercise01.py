class A:

    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value <= 200:
            self.__hp = value
        else:
            raise ValueError("错误")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value < 100:
            self.__atk = value
        else:
            raise ValueError("错误")


a = A("li", 100, 99)
print(a.__dict__)
a.hp = 200
print(a.atk)
print(a.__dict__)
