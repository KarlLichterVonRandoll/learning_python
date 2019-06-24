"""
    练习:定义生成器函数 my_enumerate
    实现下列现象
    list01 = [3, 4, 55, 6, 7]
    for item in enumerate(list01):
        print(item)
"""


def generate_index(x):
    for i in range(x):
        yield i


# list01 = [3, 4, 55, 6, 7]
#
# for item in generate_index(len(list01)):
#     print((item, list01[item]))


"""
    练习2
"""

list02 = ["sun", "zhu", "tang", "sha", "bai"]
list03 = [101, 102, 103, 104]
list04 = ["A", "B", "C"]


def my_zip(*args):
    min_len = min(list(map(len, args)))
    i = 0
    while i < min_len:
        list_ele = []
        for item in args:
            list_ele.append(item[i])
        yield tuple(list_ele)
        i += 1


# for item in my_zip(list02, list03, list04):
#     print(item)


"""
    获取列表中所有字符串、小数
    使用生成器函数，生成器表达式，列表推导式 
"""

list05 = ['a', 3.3, 'efg', 4, 5.0, 'run']


def get_element(x, ele_type):
    for item in x:
        if type(item) == ele_type:
            yield item


func01 = get_element(list05, float)
for item in func01:
    print(item)

func02 = (item for item in list05 if type(item) == str)
for item in func02:
    print(item)

list06 = [item for item in list05 if type(item) == str]
print(list06)


