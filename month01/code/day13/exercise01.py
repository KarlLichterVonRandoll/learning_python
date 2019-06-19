"""
    手雷炸了，可能伤害敌人/玩家
            还可能伤害其他事物（鸭子，房子）
"""

# class Bomb:
#     def explore(self, target):
#         print("手雷爆炸", end=" ")
#         # 如果传入的不是子类，就报错
#         if isinstance(target, Target):
#             target.injured()
#         else:
#             raise Exception
#
#
# class Target:
#     def injured(self):
#         # 如果子类不重写，则异常，强制子类重写 injured 方法
#         raise NotImplementedError
#
#
# class Enemy(Target):
#     def injured(self):
#         print("敌人爆头了")
#
#
# class Player(Target):
#     def injured(self):
#         print("玩家碎屏了")
#
#
# class Duck(Target):
#     def injured(self):
#         print("鸭子炸飞了")
#
#
# class House(Target):
#     def injured(self):
#         print("房子塌了")
#
#
# enemy = Enemy()
# player = Player()
# duck = Duck()
# house = House()
#
# bomb = Bomb()
# bomb.explore(enemy)
# bomb.explore(player)
# bomb.explore(duck)
# bomb.explore(house)


"""
    定义图形管理器类
        1.管理所有图形
        2.提供计算所有图形总面积的方法
        圆形、矩形
"""
# import math
#
#
# class GraphicalController:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_graphic(self, graphical):
#         if isinstance(graphical, Graphical):
#             self.__graphics.append(graphical)
#         else:
#             raise Exception
#
#     def get_total_area(self):
#         total_area = 0
#         for item in self.__graphics:
#             total_area += item.calculate_area()
#         return total_area
#
#
# class Graphical:
#     def calculate_area(self):
#         raise Exception
#
#
# class Circular(Graphical):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#
# class Rectangle(Graphical):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#
# circular = Circular(10)
# rectangle = Rectangle(6, 8)
#
# controller = GraphicalController()
# controller.add_graphic(circular)
# controller.add_graphic(rectangle)
# print(controller.get_total_area())


"""
    定义员工管理器
    1.管理所有员工
    2.计算所有员工工资
    员工：  程序员：底薪+项目分红
           销售：底薪 + 销售额 * 0.05
"""


class EmployeeManager:
    def __init__(self):
        self.__employee = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employee.append(employee)
        else:
            raise Exception

    def get_total_salary(self):
        total_salary = 0
        for item in self.__employee:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Sale(Employee):
    def __init__(self, base_salary, sale_volume):
        super().__init__(base_salary)
        self.sale_volume = sale_volume

    def calculate_salary(self):
        return self.base_salary + self.sale_volume * 0.05


manager = EmployeeManager()
programmer = Programmer(7000, 5000)
sale = Sale(5000, 200)

manager.add_employee(programmer)
manager.add_employee(sale)
re = manager.get_total_salary()
print(re)
