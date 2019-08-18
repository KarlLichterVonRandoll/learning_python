"""
demo02_lp.py  线性预测
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
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices = \
    np.loadtxt('aapl.csv',
               delimiter=',', usecols=(1, 3, 4, 5, 6),
               unpack=True, dtype='M8[D], f8, f8, f8, f8',
               converters={1: dmy2ymd})

# 绘制收盘价的折线图
plt.figure('AAPL', facecolor='lightgray')
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

# 基于线性预测理论，通过6天股价预测第7天的股票价格
N = 3
# 构建一个数组存储所有的预测结果
pred_prices = np.zeros(
    closing_prices.size - 2 * N + 1)
print(pred_prices.size)
for i in range(pred_prices.size):
    A = np.zeros((N, N))  # A： N*N的矩阵
    for j in range(N):
        A[j, ] = closing_prices[i + j:i + j + N]
    B = closing_prices[i + N:i + N * 2]
    X = np.linalg.lstsq(A, B)[0]
    print(X)
    pred = B.dot(X)  # 向量点乘
    pred_prices[i] = pred

# 绘制预测价格曲线
plt.plot(dates[2 * N:], pred_prices[:-1],
        'o-', label='Predict Prices',
        linewidth=2, color='orangered',
        linestyle='-', alpha=0.7)

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
