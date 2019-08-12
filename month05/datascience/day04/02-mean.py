"""
    绘制均值相关指标
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 将日月年字符串转换为年月日字符串
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


# 加载文件
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumns = \
    np.loadtxt('aapl.csv',
               delimiter=',', usecols=(1, 3, 4, 5, 6, 7),
               unpack=True, dtype='M8[D], f8, f8, f8, f8, f8',
               converters={1: dmy2ymd})

# 绘制收盘价的折线图
plt.figure('AAPL', facecolor='lightgrey')
plt.title('AAPL', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(linestyle=':')
plt.tick_params(labelsize=10)
# 设置刻度定位器
ax = plt.gca()

# 每周一一个主刻度
maloc = md.WeekdayLocator(byweekday=md.MO)
ax.xaxis.set_major_locator(maloc)
# 设置主刻度日期的格式
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d'))

# DayLocator:每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())

# 把dates的数据类型改为matplotlib的日期类型
dates = dates.astype(md.datetime.datetime)

# 绘制收盘价
plt.plot(dates, closing_prices,
         label='Closing Prices', linewidth=2,
         color='dodgerblue', linestyle='--',
         alpha=0.7)

# 绘制算数平均值的水平线
mean = np.mean(closing_prices)
plt.hlines(mean, dates[0], dates[-1], color='orangered', label='Mean(CP)')

# 绘制VWAP 成交量加权平均价格
vwap = np.average(closing_prices, weights=volumns)
plt.hlines(vwap, dates[0], dates[-1], color='green', label='VMAP')

# 绘制TWAP 时间加权平均价格
times = np.linspace(1, 6, 30)
twap = np.average(closing_prices, weights=times)
plt.hlines(twap, dates[0], dates[-1], color='red', label='TWAP')

# 绘制中位数水平线
median = np.median(closing_prices)
plt.hlines(median, dates[0], dates[-1],
           color='gold', label='median')

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
