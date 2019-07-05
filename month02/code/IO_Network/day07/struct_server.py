"""
    客户端不断录入学生信息，将其发送到服务端，
    在服务端，将学生信息写入到一个文件中，每个学生信息占一行
    信息格式： id  name  age  score
"""

import struct
from socket import *

st = struct.Struct("i6sif")

udpserver = socket(AF_INET, SOCK_DGRAM)

udpserver.bind(("0.0.0.0", 9527))

while True:
    data, addr = udpserver.recvfrom(1024)
    print("receive from", addr)

    with open("student.txt", "a") as f:
        data = st.unpack(data)  # st.unpack()返回元组 (id, name, age, score)
        info = "%d  %-3s  %d  %.1f\n" % data
        f.write(info)
        f.flush()
