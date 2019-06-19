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

