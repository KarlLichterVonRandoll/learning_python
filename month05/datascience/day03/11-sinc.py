import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ma

plt.figure("Signal", facecolor='lightgray')
plt.title("Signal", fontsize=14)
plt.xlim(0, 10)
plt.ylim(-3, 3)
plt.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = plt.plot([], [], color='dodgerblue', label='Signal')[0]

x = 0


def update(data):
    t, v = data
    x, y = pl.get_data()
    # x是保存x坐标的ndarray对象
    # y是保存y坐标的ndarray对象
    x = np.append(x, t)
    y = np.append(y, v)
    pl.set_data(x, y)
    # 移动坐标轴
    if x[-1] > 5:
        plt.xlim(x[-1] - 5, x[-1 + 5])


def y_generator():
    global x
    y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
    yield (x, y)
    x += 0.05


anim = ma.FuncAnimation(plt.gcf(), update, y_generator, interval=20)
plt.tight_layout()

plt.show()
