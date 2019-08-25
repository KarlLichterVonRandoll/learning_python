"""
数据平滑
绘制两只股票收益率曲线。收益率 =（后一天收盘价-前一天收盘价） / 前一天收盘价
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt


def dmy2ymd(dmy):
    # 把日月年字符串转为年月日字符串
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


dates, bhp_closing_prices = \
    np.loadtxt('bhp.csv',
               delimiter=',', usecols=(1, 6),
               dtype='M8[D], f8',
               converters={1: dmy2ymd}, unpack=True)

vale_closing_prices = \
    np.loadtxt('aapl.csv',
               delimiter=',', usecols=(6,),
               dtype='f8', unpack=True)

bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

# 绘制这条曲线
plt.figure('BHP VALE RETURNS', facecolor='lightgray')
plt.title('BHP VALE RETURNS', fontsize=20)
plt.xlabel('Date')
plt.ylabel('Price')
ax = plt.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y %m %d'))
dates = dates.astype(md.datetime.datetime)
# 绘制收益线
plt.plot(dates, bhp_returns,
         color='red', linestyle='--',
         label='bhp_returns', alpha=0.1)
plt.plot(dates, vale_returns,
         color='black', linestyle='--',
         label='vale_returns', alpha=0.1)

# 卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')
# 绘制卷积降噪线
plt.plot(dates[7:], bhp_returns_convolved,
         color='dodgerblue',
         label='bhp_returns_convolved', alpha=0.2)
plt.plot(dates[7:], vale_returns_convolved,
         color='orangered',
         label='vale_returns_convolved', alpha=0.2)

# 拟合这两条曲线，获取两组多项式系数
days = dates.astype('M8[D]').astype('int32')
bhp_p = np.polyfit(
    days[7:], bhp_returns_convolved, 3)
bhp_polyfit_y = np.polyval(bhp_p, days[7:])
vale_p = np.polyfit(
    days[7:], vale_returns_convolved, 3)
vale_polyfit_y = np.polyval(vale_p, days[7:])
# 绘制拟合线
plt.plot(dates[7:], bhp_polyfit_y,
         color='dodgerblue', label='bhp_returns_polyfit')
plt.plot(dates[7:], vale_polyfit_y,
         color='orangered', label='vale_returns_polyfit')

# 求两条曲线的交点  f(bhp) = f(vale)的根
sub_p = np.polysub(bhp_p, vale_p)
roots_x = np.roots(sub_p)  # 让f(bhp) - f(vale) = 0
print(roots_x.astype('M8[D]'))

plt.legend()
plt.gcf().autofmt_xdate()
plt.show()
