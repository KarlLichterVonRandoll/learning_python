"""
    客户端不断录入学生信息，将其发送到服务端，
    在服务端，将学生信息写入到一个文件中，每个学生信息占一行
    信息格式： id  name  age  score
"""

import struct
from socket import *

st = struct.Struct("i6sif")

udpsocket = socket(AF_INET, SOCK_DGRAM)

addr = ("127.0.0.1", 9527)

while True:
    id = int(input("输入id:"))
    name = input("输入姓名:").encode()
    age = int(input("输入年龄:"))
    score = float(input("输入成绩:"))

    data = st.pack(id, name, age, score)

    udpsocket.sendto(data, addr)
