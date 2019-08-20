"""
    线性拟合趋势线
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
lowest_prices, closing_prices = \
    np.loadtxt('aapl.csv',
               delimiter=',',
               usecols=(1, 3, 4, 5, 6),
               unpack=True,
               dtype='M8[D], f8, f8, f8, f8',
               converters={1: dmy2ymd}
               )

# 绘制收盘价折线图
plt.figure('AAPL', facecolor='lightgray')
plt.title('AAPL', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(linestyle=":")
plt.tick_params(labelsize=10)

# 设置刻度定位器
ax = plt.gca()

# 每周一一个主刻度
maloc = md.WeekdayLocator(byweekday=md.MO)
ax.xaxis.set_major_locator(maloc)

# 设置主刻度日期的格式
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d')
)

# DayLocator:每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())

# 把dates的数据类型改为matplotlib的日期类型
dates = dates.astype(md.datetime.datetime)

# 绘制收盘价
plt.plot(dates, closing_prices,
         label='Closing Prices', linewidth=2,
         color='dodgerblue', linestyle='--',
         alpha=0.3)

# 绘制所有趋势点
trend_points = (highest_prices + lowest_prices + closing_prices) / 3
plt.scatter(dates, trend_points,
            color='orangered', s=60,
            label='Trend Points')

# 针对30个趋势点，拟合得到一条趋势线
days = dates.astype('M8[D]').astype('int32')
A = np.column_stack((days, np.ones(days.size)))
B = trend_points
X = np.linalg.lstsq(A, B)[0]
print(X)
pred_y = X[0] * days + X[1]

plt.plot(dates, pred_y, color='red',
         label='Trend Line')

plt.legend()
plt.gcf().autofmt_xdate()

plt.show()
