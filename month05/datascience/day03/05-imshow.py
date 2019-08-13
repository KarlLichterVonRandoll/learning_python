import numpy as np
import matplotlib.pyplot as plt

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
#  根据一个奇妙的公式算出每个坐标点的高度值z
z = (1 - x / 2 + x ** 5 + y ** 3) * \
    np.exp(-x ** 2 - y ** 2)
# 绘制
plt.figure('Imshow', facecolor='lightgray')
plt.title('Imshow')
plt.grid(linestyle=':')
plt.imshow(z, cmap='jet', origin='lower')
plt.colorbar()
plt.show()
