import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2

plt.figure("Fill", facecolor="lightgray")
plt.title("Fill")

# 绘制曲线
plt.plot(x, sinx, color="dodgerblue", label='sinx', linewidth=2)
plt.plot(x, cosx, color="orangered", label='cosx', linewidth=2)

# 绘制填充
plt.fill_between(x, sinx, cosx, sinx > cosx, color='dodgerblue', alpha=0.5)
plt.fill_between(x, sinx, cosx, sinx < cosx, color='orangered', alpha=0.5)

plt.legend()
plt.show()
