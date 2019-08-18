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

# 实现加权卷积
# 通过指数函数，寻求一组卷积核
kernel = np.exp(np.linspace(-1, 0, 5))
kernel = kernel[::-1]
kernel /= kernel.sum()
sma53 = np.convolve(
    closing_prices, kernel, 'valid')
plt.plot(dates[4:], sma53,
         label='SMA-5(3)', linewidth=1,
         color='violet', linestyle='-')

# 绘制5日均线的布林带
stds = np.zeros(sma53.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
lowers = sma53 - 2 * stds
uppers = sma53 + 2 * stds
plt.plot(dates[4:], uppers,
         label='Upper', linewidth=1,
         color='orangered', linestyle='-')
plt.plot(dates[4:], lowers,
         label='Lower', linewidth=1,
         color='orangered', linestyle='-')
plt.fill_between(dates[4:], uppers,
                 lowers, uppers > lowers, color='orangered',
                 alpha=0.3)

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
