"""
    从列表中选出所有偶数
    使用生成器
"""

list01 = [4, 5, 566, 7, 8, 10]
result = []


def get_even_num(x):
    for i in x:
        if i % 2 == 0:
            yield i


func = get_even_num(list01)
print(type(func))
for item in func:
    result.append(item)
print(result)




