"""
    编写一个文件拷贝程序，从终端输入一个文件，
　　　　　将文件保存在当前目录下

        * 文件类型不确定（可是文本文件，可能是二进制文件）
"""
dir_name = input(":")
f1 = open(dir_name, "rb")
f2 = open("new_" + dir_name, "wb")

for l in f1:
    f2.write(l)

f1.close()
f2.close()
