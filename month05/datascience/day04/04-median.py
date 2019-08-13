import numpy as np

closing_prices = np.loadtxt("aapl.csv",
                            delimiter=",", usecols=(6), unpack=True)
size = closing_prices.size

sorted_price = np.msort(closing_prices)
median = (sorted_price[int((size - 1) / 2)] + sorted_price[int(size / 2)]) / 2
print(median)
median = np.median(sorted_price)
print(median)
