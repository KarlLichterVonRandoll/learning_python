"""
    需求:
      实现对学生信息的增加、删除、修改和查询。
    分析:
      界面可能使用控制台，也可能使用Web等等。
        1. 识别对象：
          界面视图类     逻辑控制类     数据模型类
        2. 分配职责：
          界面视图类：负责处理界面逻辑，比如显示菜单，获取输入，显示结果等。
          逻辑控制类：负责存储学生信息，处理业务逻辑。比如添加、删除等
          数据模型类：定义需要处理的数据类型。比如学生信息。
        3. 建立交互：
          界面视图对象  <----> 数据模型对象   <---->  逻辑控制对象
"""

"""
    设计
      数据模型类：StudentModel	
        数据：编号 id,姓名 name,年龄 age,成绩 score 
      逻辑控制类：StudentManagerController	
        数据：学生列表 __stu_list 
        行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，
             修改学生update_student，根据成绩排序order_by_score。
      界面视图类：StudentManagerView
        数据：逻辑控制对象__manager
        行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
             输入学生__input_students，输出学生__output_students，
             删除学生__delete_student，修改学生信息__modify_student，
             按成绩输出学生__output_student_by_score
"""


# 数据模型类
class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", age=0, score=0.0, id=0):
        """
            创建学生对象
        :param name: 姓名 str
        :param age: 年龄 int
        :param score: 成绩 float
        :param id: 学生对象的唯一标识 int
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value


# 逻辑控制类
class StudentManageController:
    # 类变量，初始编号
    __init_id = 1000
    a = 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 学生对象组成的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加学生对象
        :param stu_info: 学生对象
        :return:
        """
        stu_info.id = StudentManageController.__generate_id()
        self.__stu_list.append(stu_info)

    @staticmethod
    def __generate_id():
        """
            生成学生id
        :return: 学生id int
        """
        StudentManageController.__init_id += 1
        return StudentManageController.__init_id

    def remove_student(self, stu_id):
        """
            # 根据id移除学生
        :param stu_id: 学生id int
        :return: True or False
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_info):
        """
            修改指定id的学生信息
        :param stu_info: 学生对象
        :return: True or False
        """
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list)):
            for j in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]


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


"""
# 测试添加学生功能
stu01 = StudentModel("张无忌", 26, 95)
stu02 = StudentModel("张三丰", 130, 100)
stu03 = StudentModel("赵敏", 23, 80)
stu04 = StudentModel("周芷若", 24, 90)
stu05 = StudentModel("谢逊", 60, 85)

manager01 = StudentManageController()
manager01.add_student(stu01)
manager01.add_student(stu02)
manager01.add_student(stu03)
manager01.add_student(stu04)
manager01.add_student(stu05)

# 测试成绩排序功能
manager01.order_by_score()

for item in manager01.stu_list:
    print(item.name, item.age, item.score, item.id)

# 测试删除学生功能
print("删除", manager01.remove_student(1001))

# 测试修改学生功能
stu_new = StudentModel("赵敏", 25, 82, 1003)
print("修改", manager01.update_student(stu_new))

for item in manager01.stu_list:
    print(item.name, item.age, item.score, item.id)
"""

# 测试
view = StudentManagerView()
view.main()
