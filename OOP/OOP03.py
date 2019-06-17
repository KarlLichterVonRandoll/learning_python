"""
学生管理系统
"""
class StudentModel():
    """
        学生数据模型类
    """
    def __init__(self, name="", age=0, score=0, id=0):
        self.__name = name
        self.__age = age
        self.__score = score
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

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

class StudentManagerController():
    """
        学生逻辑管理类
    """
    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self, stu):
        """
            添加新学生
        :param stu:  需要添加的学生对象
        """
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def __generate_id(self):
        # 生成编号的需求:新编号,比上次添加的对象编号多1.
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id + 1
        # else:
        #     id = 1
        # return id
        return self.__list_stu[-1].id + 1 if len(self.__list_stu) > 0 else 1



student01 = StudentModel("Tony",23,100,123654789)
print(student01.id)