import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     passwd="123456",
                     database="students",
                     charset="utf8")

cur = db.cursor()

data_list = []
for i in range(2000000):
    name = 'Tom_%s' % i
    if i % 1000 == 0:
        print(i)
    data_list.append(name)

ins = "insert into student(name) values(%s)"

cur.executemany(ins, data_list)
db.commit()

cur.close()
db.close()
