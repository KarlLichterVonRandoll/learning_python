import redis

# 创建数据库连接对象
r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                password='123456')

# 通用命令示例
# 查看所有的key，返回列表
key_list = r.keys('*')
for i in key_list:
    print(i.decode())

# 查看key数据类型 b'list'
# print(r.type('mylist'))

# 判断key是否存在，返回值 0 | 1
# print(r.exists('mylist'))

# 设置key过期时间, mylist 5 秒后过期
# r.expire('mylist', 5)

# 删除key
# r.delete('mylist2', 'age')






