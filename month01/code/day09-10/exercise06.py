# 获取学生信息
student_info = input("输入学生年龄信息：")

# 输入信息预处理
stu_list = student_info.replace(" ", "").split(";")
for i in range(len(stu_list)):
    if stu_list[i] == "":
        del stu_list[i]

# 按指定格式打印学生信息
for item in stu_list:
    item_list = item.split(",")
    print("{:<20}:{:0>2};".format(item_list[0], item_list[1]))
