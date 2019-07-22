"""
    服务端
"""

from socket import *
import pymysql

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ADDR = ("0.0.0.0", 8888)

s.bind(ADDR)
s.listen(10)

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="dict",
                     charset="utf8")

cur = db.cursor()


def register(name, passwd):
    sql = "select * from user where user=%s"
    cur.execute(sql, [name])

    if cur.fetchone():
        return "用户名重复"
    try:
        sql = "insert into user (user, passwd) values(%s, %s)"
        cur.execute(sql, [name, passwd])
        db.commit()
        return "注册成功"
    except Exception as e:
        db.rollback()
        print(e)
    pass


def login(name, passwd):
    sql01 = "select * from user where user=%s and passwd=%s"
    cur.execute(sql01, [name, passwd])

    if cur.fetchone():
        return "登录成功 !"
    else:
        return "登录失败 !"


def main():
    while True:
        connfd, addr = s.accept()
        print("connect from", addr)

        while True:
            data = connfd.recv(1024).decode()
            if data == "1":
                connfd.send(b'ok')
                data = connfd.recv(1024).decode()
                name = data.split(",")[0]
                passwd = data.split(",")[1]
                res = register(name, passwd)
                connfd.send(res.encode())





        # connfd.close()
