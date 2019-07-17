"""
    二进制文件存储
"""

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="student",
                     charset="utf8")

cur = db.cursor()

# 存储图片
# with open('img01.jpg', 'rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image=%s where name='luna';"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class where name='luna'"
cur.execute(sql)
data = cur.fetchone()  # 返回元组
with open('img02.jpg', 'wb') as f:
    f.write(data[0])

# 关闭数据库
cur.close()
db.close()
