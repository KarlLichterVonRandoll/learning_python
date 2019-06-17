class Wife:
    number_of_wife = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Wife.number_of_wife += 1
        Wife.print_wife_count()

    @classmethod
    def print_wife_count(cls):
        print("Wife对象个数为 %d 个" % cls.number_of_wife)

    def print_name(self):
        print(self.name)


list01 = [
    Wife("赵敏", 24),
    Wife("周芷若", 25),
    Wife("小昭", 22),
    Wife("蛛儿", 23)
]

Wife.print_wife_count()
print(list01[0].number_of_wife)


