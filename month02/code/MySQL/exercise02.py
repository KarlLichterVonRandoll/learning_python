"""
    编写程序模拟注册和登录过程
    * 创建一个 user 表 包含 用户名和密码字段
    * 应用程序中模拟注册和登录功能
      注册则输入用户名和密码存入到数据库
        （用户名不能重复）

      登录则进行数据库比对，如果有该用户则打印登录成功否则让重写输入
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="stu",
                     charset="utf8")

cur = db.cursor()


def register():
    name = input("Name:")
    passwd = input("Passwd:")
    sql01 = "select * from user where user=%s"
    cur.execute(sql01, [name])

    if cur.fetchone():
        print("用户名重复")
        return
    try:
        sql = "insert into user (user, passwd) values(%s, %s)"
        cur.execute(sql, [name, passwd])
        db.commit()
        print("注册成功")
    except Exception as e:
        db.rollback()
        print(e)


def login():
    name = input("Name:")
    passwd = input("Passwd:")
    sql01 = "select * from user where user=%s and passwd=%s"
    cur.execute(sql01, [name, passwd])

    if cur.fetchone():
        print("登录成功 !")
    else:
        print("登录失败 !")


if __name__ == "__main__":
    while True:
        print("""
        ============
        1.注册 2.登录
        ============
        """)
        cmd = input("输入命令:")
        if cmd == '1':
            # 执行注册
            register()
        elif cmd == '2':
            # 执行登录
            login()
