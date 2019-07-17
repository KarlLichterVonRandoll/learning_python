"""
    pymysql 操作数据库流程演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="student",
                     charset="utf8")

# 创建游标对象,(操作数据库，执行 sql 语句)
cur = db.cursor()

# 执行 sql 语句
sql = "insert into class values \
    (7, 'Emma', 17, 'w', 75.5, '2019-9-9')"

cur.execute(sql)  # 执行语句

db.commit()  # 将写操作提交，多次写操作一同提交

# 关闭数据库
cur.close()
db.close()
