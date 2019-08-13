import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 把日月年字符串转为年月日字符串
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


# 加载文件
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, \
volumns = np.loadtxt('aapl.csv',
                     delimiter=',', usecols=(1, 3, 4, 5, 6, 7),
                     unpack=True, dtype='M8[D], f8, f8, f8, f8, f8',
                     converters={1: dmy2ymd})

# 求最值: 返回一个数组中最大值/最小值/极差
print('max:', np.max(highest_prices))
print('min:', np.min(lowest_prices))
print('ptp:', np.ptp(highest_prices))
# 返回一个数组中最大/最小元素的下标
maxi = np.argmax(highest_prices)
mini = np.argmin(lowest_prices)
print(maxi, mini)
print('max date:', dates[maxi])
print('min date:', dates[mini])

a = np.arange(1, 10)
b = a[::-1]
a = a.reshape(3, 3)
b = b.reshape(3, 3)
print(a)
print(b)
# 将两个同维数组中对应元素中最大/最小元素构成一个新的数组
print(np.maximum(a, b))
print(np.minimum(a, b))
