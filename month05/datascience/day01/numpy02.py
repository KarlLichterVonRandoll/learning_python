"""
    numpy 自定义复合类型
"""

import numpy as np

data = [('a', [1, 2, 3], 11),
        ('b', [4, 5, 6], 12),
        ('c', [7, 8, 9], 13)]

# 第一种 dtype 设置方式
ary01 = np.array(data, dtype='U2, 3int32, int32')
print(ary01.dtype)
print(ary01[0]['f0'])
print(ary01[1]['f1'])

# 第二种 dtype 设置方式
ary02 = np.array(data, dtype=[('name', 'str', 2),
                              ('score', 'int32', 3),
                              ('age', 'int32', 1)])
print(ary02.dtype)
print(ary02[0]['name'])
print(ary02[1]['age'])

# 第三种 dtype 设置方式
ary03 = np.array(data, dtype={'names': ['name', 'scores', 'age'],
                              'formats': ['U2', '3int32', 'int32']})
print(ary03.dtype)
print(ary03[0]['age'])  # 返回 a 的年龄
print(ary03[2]['scores'])  # 返回 c 的成绩

# 第四种 dtype 设置方式
ary04 = np.array(data, dtype={'name': ('U3', 0),
                              'scores': ('3int32', 16),
                              'age': ('int32', 28)})
print(ary04.dtype)
print(ary04[0]['name'], ary04[0]['scores'], ary04.itemsize)

# ndarray数组存放日期数据
dates = ['2011-01-01', '2012-01-01',
         '2011-02-01', '2012',
         '2011-01-01 10:10:10']
ary = np.array(dates)
print(ary, ary.dtype)
ary = ary.astype('M8[D]')
print(ary, ary.dtype, ary[1] - ary[0])
