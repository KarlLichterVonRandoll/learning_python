from bll import StudentManageController
from model import StudentModel
from error import *


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
        while True:
            name_str = input("输入姓名:")
            if name_str != "":
                try:
                    item = int(name_str)
                except Exception:
                    name = name_str
                    break
                else:
                    print("姓名必须是字符串")
                    continue
            else:
                print("姓名不能为空")
        while True:
            age_str = input("输入年龄:")
            try:
                age = int(age_str)
            except Exception:
                print("请输入数字")
                continue
            else:
                break
        while True:
            score_str = input("输入成绩:")
            try:
                score = float(score_str)
            except Exception:
                print("请输入数字")
                continue
            else:
                if 0 <= score <= 100:
                    break
                else:
                    print("超出范围")

        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self):
        for item in self.__manager.stu_list:
            print("姓名:", item.name, "年龄:", item.age, "成绩:", item.score, "id:", item.id)

    def __delete_students(self):
        while True:
            try:
                id = int(input("输入学生id:"))
            except Exception:
                print("请输入数字id")
            else:
                break
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_students(self):
        while True:
            try:
                id = int(input("输入需要修改学生的id:"))
            except Exception:
                print("请输入数字id")
            else:
                leap = 0
                for item in self.__manager.stu_list:
                    if item.id == id:
                        leap = 1
                if leap:
                    break
                else:
                    print("id 不存在")
        while True:
            name_str = input("输入新的姓名:")
            if name_str != "":
                try:
                    item = int(name_str)
                except Exception:
                    name = name_str
                    break
                else:
                    print("姓名必须是字符串")
                    continue
            else:
                print("姓名不能为空")
        while True:
            age_str = input("输入新的年龄:")
            try:
                age = int(age_str)
            except Exception:
                print("请输入数字")
                continue
            else:
                break
        while True:
            score_str = input("输入新的成绩:")
            try:
                score = float(score_str)
            except Exception:
                print("请输入数字")
                continue
            else:
                if 0 <= score <= 100:
                    break
                else:
                    print("超出范围")
        stu = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()
