from bll import StudentManageController
from model import StudentModel


# 界面视图类
class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManageController()

    @staticmethod
    def __display_menu():
        print("(1)添加学生")
        print("(2)显示学生")
        print("(3)删除学生")
        print("(4)修改学生")
        print("(5)按照成绩输出学生")

    def __select_menu(self):
        item = input("输入选项:")
        if item == "1":
            self.__input_students()
        if item == "2":
            self.__output_students()
        if item == "3":
            self.__delete_students()
        if item == "4":
            self.__modify_students()
        if item == "5":
            self.__output_student_by_score()
        if item == "":
            exit()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        name = input("输入姓名:")
        age = int(input("输入年龄:"))
        score = float(input("输入成绩:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self):
        for item in self.__manager.stu_list:
            print("姓名:", item.name, "年龄:", item.age, "成绩:", item.score, "id:", item.id)

    def __delete_students(self):
        id = int(input("输入学生id:"))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_students(self):
        id = int(input("输入要修改学生的id"))
        name = input("输入新的姓名:")
        age = int(input("输入新的年龄:"))
        score = float(input("输入新的成绩:"))
        stu = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()


