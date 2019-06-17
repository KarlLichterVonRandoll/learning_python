class Student:
    # 数据成员
    def __init__(self, name, age):
        # self: 调用当前方法的对象的地址
        self.name = name
        self.age = age
        print("My name is %s, i'm %d years old" % (self.name, self.age))

    # 行为成员
    def study(self):
        print(self.name + " is studying")


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def run(self, speed):
        print("%s is running, the speed is %d km/h" % (self.model, speed))


# 创建对象,实际调用__init__方法
stu01 = Student("Bob", 18)
stu01.study()
stu02 = Student("lili", 16)
stu02.study()

car01 = Car("Tesla", 100000)
car01.run(100)
car02 = Car("BMW", 350000)
print(car02.price)
