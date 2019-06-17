"""
    创建学生类
    -- 数据：姓名、年龄、成绩、性别
    -- 行为：打印个人信息
"""


class Student:
    def __init__(self, name, age, score, sex=None):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_info(self):
        print("姓名：%s,年龄：%d,成绩：%d,性别：%s"
              % (self.name, self.age, self.score, self.sex))


"""
    循环录入学生信息，如果是空字符串退出
    在控制台中输出每个学生信息
    打印第一个学生信息
"""
stu_list = [
    Student("托尼斯塔克", 50, 100, "男"),
    Student("娜塔莎罗曼诺夫", 35, 80, "女"),
    Student("彼得帕克", 19, 85, "男"),
    Student("索尔", 1500, 90, "男"),
    Student("史蒂夫罗杰斯", 90, 80, "男"),
]


# while True:
#     name_input = input("输入学生姓名：")
#     if name_input == "":
#         break
#     age_input = int(input("输入学生年龄："))
#     score_input = int(input("输入学生成绩："))
#     sex_input = input("输入学生性别：")
#     stu = Student(name_input, age_input, score_input,sex_input)
#     stu_list.append(stu)

# 查找指定人名
def find01(obj_list, name):
    for obj in obj_list:
        if obj.money == name:
            return obj


# 查找所有女同学
def find02():
    for item in stu_list:
        if item.sex == "女":
            item.print_info()


# 统计年龄30以上的学生数量
def count01():
    count = 0
    for item in stu_list:
        if item.age >= 30:
            count += 1
    return count


# 将所有学生的成绩归零
def set01():
    for item in stu_list:
        item.score = 0


# 获取所有人的名字
def get01():
    for item in stu_list:
        print(item.name)


# 查找年龄最大的学生
def find03():
    max_stu = stu_list[0]
    for i in range(1, len(stu_list)):
        if stu_list[i].age > max_stu.age:
            max_stu = stu_list[i]
    print(max_stu.name, max_stu.age)


find03()
