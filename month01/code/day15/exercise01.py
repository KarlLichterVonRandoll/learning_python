"""
    时间处理
"""
import time

# 1.获取当前时间戳(从1970.01.01 00:00开始经过的秒数)
print(time.time())

# 2.时间元组
# 时间戳 -> 时间元组
tuple_time = time.localtime()

# 时间元组 -> 时间戳
print(time.mktime(tuple_time))

# 时间元组 -> str
str_time = time.strftime("%Y / %m / %d %H:%M:%S", tuple_time)
print(str_time)

# str -> 时间元组
print(time.strptime(str_time, "%Y / %m / %d %H:%M:%S"))
