"""
    ("孙悟空","猪八戒","唐僧")
    使用迭代器遍历元组
"""
tuple01 = ("孙悟空", "猪八戒", "唐僧")

iter01 = tuple01.__iter__()
while True:
    try:
        item = iter01.__next__()
        print(item)
    except StopIteration:
        break

"""
    {"孙悟空": 1, "猪八戒": 2, "唐僧": 3}
    不使用for,获取字典所有数据
"""
dict01 = {"孙悟空": 1, "猪八戒": 2, "唐僧": 3}

iter02 = dict01.__iter__()
while True:
    try:
        item = iter02.__next__()
        print(item, dict01[item])
    except StopIteration:
        break

for i in range(9):
    pass