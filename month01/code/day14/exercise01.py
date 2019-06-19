class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 对象 --> 字符串(任意格式)
    def __str__(self):
        return "我叫 %s" % self.name

    # 对象 --> 字符串(解释器可识别，有格式)
    def __repr__(self):
        return 'Student("%s", %d)' % (self.name, self.age)


# 克隆对象
stu01 = Student("peter", 17)
# repr 返回python格式的字符串
str02 = repr(stu01)
print(str02)
# eval 根据字符串执行代码
stu02 = eval(str02)
print(stu02)
