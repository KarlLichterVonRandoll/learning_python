"""
    定义函数：获取成绩的函数
    如果异常，继续获取成绩，直到获取正确成绩
    成绩必须在0-100之间
"""


def get_score():
    while True:
        str_result = input("输入成绩:")
        try:
            score = int(str_result)
        except Exception:
            print("输入整数")
            continue
        if 0 <= score <= 100:
            return score
        else:
            print("超出范围")


# print(get_score())

class AgeError(Exception):
    def __init__(self, message, age_value, id, code_line):
        self.message = message
        self.age_value = age_value
        self.id = id
        self.code_line = code_line


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 21 <= value <= 30:
            self.__age = value
        else:
            raise AgeError("年纪太大了", value, 404, 20)

try:
    wife = Wife(81)
except AgeError as e:
    print(e.message)
    print(e.age_value)
    print("重新输入")
