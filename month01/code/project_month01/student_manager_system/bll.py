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
        for i in range(len(self.__stu_list)-1):
            for j in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[j].score:
                    self.__stu_list[i], self.__stu_list[j] = self.__stu_list[j], self.__stu_list[i]


