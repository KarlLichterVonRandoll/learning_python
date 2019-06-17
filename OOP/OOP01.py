# class Dog(object):
#     # __init__方法是一个特殊方法，每次创建新实例的时候就会自动调用这个方法
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(self.name + " is eating!")
#
#
# dog = Dog("aaa")
# print(dog.name)
# dog.eat()


# class Student():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("你好，%s同学" % self.name)
#         self.number = 15632548753
#
#     def update_number(self, new_number):
#         self.number = new_number
#
# student01 = Student("Bob", 10)
# student01.update_number(55667788)
# print(student01.number)


class Car(object):

    def __init__(self, model="BMW", year=2019, foo='abc'):
        self.model = model
        self.year = year
        self.__foo = foo

    def run(self):
        print("the car is running")

class ElectricCar(Car):

    def __init__(self):
        super().__init__()
        self.model = "Tesla"
        self.battery_size = 70

    def run(self):
        print("the car is running on the road!")


# car = ElectricCar()
# print(car.battery_size)
# car.run()
car = Car()
print(car.__foo)
