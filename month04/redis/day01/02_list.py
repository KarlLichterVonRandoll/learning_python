import redis

r = redis.Redis(host='127.0.0.1',
                port=6379,
                db=0,
                password='123456')

# 列表操作
# 创建列表  ['laoqi', 'maria', 'laoguo', 'laowei']
r.rpush('teachers', 'laoqi', 'maria', 'laoguo')
r.rpush('teachers', 'laowei')

# 在maria 后面加入 laotao
r.linsert('teachers', 'after', 'maria', 'laotao')


# 打印长度
print(r.llen('teachers'))

# 查看所有元素
print(r.lrange('teachers', 0, -1))

# 弹出一个元素
print(r.rpop('teachers'))

# 保留指定范围元素
r.ltrim('teachers', 0, 2)

# 阻塞弹出
while True:
    result = r.brpop('teachers', 3)
    if not result:
        break
    print(result)

r.expire('teachers', 5)

