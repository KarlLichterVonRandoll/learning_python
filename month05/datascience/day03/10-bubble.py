"""
    动画绘制
    气泡动画
"""

import matplotlib.animation as ma
import matplotlib.pyplot as plt
import numpy as np

# 构建100个泡泡，整理属性字段
n = 100
balls = np.zeros(100, dtype=[
    ('position', float, 2),  # 位置（水平位置和垂直位置）
    ('size', float, 1),  # 大小
    ('growth', float, 1),  # 生长速度
    ('color', float, 4)])  # 颜色 rgba值

# 初始化所有ball的属性值
# 随机生成最小值为0，最大值为1的n行2列的数组
# 用于 初始化所有ball的坐标
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

plt.figure("Animation", facecolor="lightgray")
plt.title("Animation", fontsize=16)
# plt.xticks([])
# plt.yticks([])
sc = plt.scatter(balls['position'][:, 0],
                 balls['position'][:, 1], balls['size'],
                 color=balls['color'])


def update(number):
    balls['size'] += balls['growth']
    # 每次让一个气泡破裂，随机生成一个新的
    ind = number % n
    balls[ind]['size'] = np.random.uniform(40, 70, 1)
    balls[ind]['position'] = np.random.uniform(0, 1, (1, 2))
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(plt.gcf(), update, interval=30)

plt.show()
