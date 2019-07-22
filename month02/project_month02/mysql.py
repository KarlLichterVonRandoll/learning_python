"""
    数据库操作模块
"""

import pymysql
import hashlib

SALT = "#aptx*"  # 盐


class Database:
    def __init__(self, host="localhost", port=3306, user="root",
                 passwd="123456", charset="utf8", database=None, ):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_database()  # 连接数据库

    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    def close(self):
        self.db.close()

    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self, name, passwd):
        sql = "select * from user where name=%s"
        self.cur.execute(sql, [name])
        # 查找到用户存在
        if self.cur.fetchone():
            return False

        hash = hashlib.md5((name + SALT).encode())  # 加盐处理
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 加密后的密码

        # 插入数据库
        try:
            sql = "insert into user (name, passwd) values(%s, %s)"
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(e)
            return False

    def login(self, name, passwd):

        hash = hashlib.md5((name + SALT).encode())  # 加盐处理
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 加密后的密码

        sql = "select * from user where name=%s and passwd=%s"
        self.cur.execute(sql, [name, passwd])

        # 有数据允许登录
        if self.cur.fetchone():
            return True
        else:
            return False

    def search(self, word):

        sql = "select comment from words where word=%s"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        # 如果找到　r --> (comment)
        if r:
            return r[0]

    def insert_history(self, name, word):

        sql = "insert into history (name, word) values (%s, %s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def history(self, name):
        sql = "select word,time from history where name=%s;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchall()

        if r:
            return r
