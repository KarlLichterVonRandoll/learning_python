import numpy as np
import matplotlib.pyplot as plt

n = 1000

# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))

# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
plt.figure('Contourf', facecolor='lightgrey')
plt.title('Contourf', fontsize=20)
plt.xlabel('x')
plt.ylabel('y')

plt.tick_params(labelsize=10)
plt.grid(linestyle=':')

# 绘制等高线图
cntr = plt.contour(x, y, z, 8, colors='black', linewidths=0.5)
# 填充等高线图
plt.contourf(x, y, z, 8, cmap='jet')

# 为等高线图添加高度标签
plt.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)

plt.show()
