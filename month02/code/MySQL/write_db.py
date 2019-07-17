"""
    pymysql 写操作  insert update delete
"""
import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="student",
                     charset="utf8")

cur = db.cursor()

# sql = "update class set score=99.5 where name='Emma'"

try:
    # 插入操作
    # name = input("Name:")
    # age = input("Age:")
    # sex = input("Sex:")
    # score = input("Score:")

    # 将变量插入 sql 语句
    # sql = "insert into class (name, age, sex, score) values('%s', %s, '%s', %s)" \
    #      % (name, age, sex, score)

    # sql = "insert into class (name, age, sex, score) values(%s, %s, %s, %s)"
    # cur.execute(sql, [name, age, sex, score])

    # 修改操作
    # sql = "update class set age=30 where name='harley'"

    # 删除操作
    sql = "delete from class where age > 80"
    cur.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()  # 回滚操作
    print(e)

cur.close()
db.close()
