import numpy as np
import datetime as dt


# 转换器函数
def dmy2wday(dmy):
    dmy = str(dmy, encoding="utf-8")
    date = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    wday = date.weekday()
    print(wday)
    return wday


wdays, closing_prices = np.loadtxt(
    "aapl.csv", delimiter=",",
    usecols=(1, 6), unpack=True,
    converters={1: dmy2wday}
)

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = closing_prices[wdays == wday].mean()

for wday, ave_closing_price in zip(
        ['MON', 'TUE', 'WED', 'THU', 'FRI'],
        ave_closing_prices):
    print(wday, np.round(ave_closing_price, 2))
