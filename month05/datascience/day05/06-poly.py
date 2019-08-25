"""
    多项式拟合：使用多项式函数拟合两只股票bhp、aapl的差价函数
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 把日月年字符串转为年月日字符串
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


# 加载文件
dates, bhp_closing_prices = \
    np.loadtxt('bhp.csv',
               delimiter=',', usecols=(1, 6),
               unpack=True, dtype='M8[D], f8',
               converters={1: dmy2ymd})
vale_closing_prices = \
    np.loadtxt('aapl.csv',
               delimiter=',', usecols=(6,),
               unpack=True)

# 绘制折线图
plt.figure('COV', facecolor='lightgray')
plt.title('COV', fontsize=18)
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

# 绘制差价
diff_prices = bhp_closing_prices - vale_closing_prices
plt.plot(dates, diff_prices, color='red', alpha=0.4)

# 多项式拟合
days = dates.astype('M8[D]').astype('int32')
P = np.polyfit(days, diff_prices, 4)  # 根据一组样本，并给出最高次幂，求出拟合多项式函数
# 计算每一天的预测值
y = np.polyval(P, days)
plt.plot(dates, y, color='green', label='polyfit')

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
