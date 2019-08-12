import numpy as np
import matplotlib.pyplot as plt

# 绘制柱状图
apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
plt.figure("Bar", facecolor="lightgray")
plt.title("Bar")

plt.xlabel("Month", fontsize=14)
plt.ylabel("Price", fontsize=14)

plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
plt.ylim((0, 40))

x = np.arange(len(apples))

plt.bar(x-0.2, apples, 0.4, color='dodgerblue', label='Apple')
plt.bar(x+0.2, oranges, 0.4, color='orangered', label='Oranger', alpha=0.75)

plt.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.show()
