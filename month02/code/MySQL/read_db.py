"""
    read_db.py
"""
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="student",
                     charset="utf8")

cur = db.cursor()

# 获取数据库数据
sql = "select name,age from class where sex='m';"
cur.execute(sql)  # 执行正确后 cur 调用函数获取结果

# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)  # 元组

# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)

# 获取所有查询结果
all_row = cur.fetchall()
for item in all_row:
    print(item)

# 关闭数据库
db.close()
cur.close()
