"""
    将单词本存入数据库

    1. 创建数据库 dict  (utf8)
    2. 创建数据表 words 将单词和单词解释分别存入不同字段
    3. 将单词存入 words 单词表 超过 19500 即可
"""
import pymysql
import re
import time

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="dict",
                     charset="utf8")

cur = db.cursor()

f = open('dict.txt')
start = time.time()
i = 1
for line in f:
    word = line.split(" ")[0]
    mean = " ".join(line.split(" ")[1:]).strip()
    # res = re.findall(r"(\S+)\s+(.+)", line)[0]
    # print(type(res))
    res = (word, mean)
    try:
        sql = "insert into words (word, comment) values(%s, %s)"
        cur.execute(sql, res)
        db.commit()
        print(i)
        i += 1
    except Exception as e:
        db.rollback()
        print(e)
cur.close()
db.close()
print(time.time() - start)

