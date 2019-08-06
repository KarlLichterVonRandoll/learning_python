import numpy as np
import matplotlib.pyplot as plt

# 绘制正弦曲线
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
y2 = np.cos(x) * 0.5
# 设置坐标轴可视区域
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.5, 1.5)
# 设置坐标轴刻度
xval = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
xtext = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$']
plt.xticks(xval, xtext)
plt.yticks([-1, -0.5, 0, 0.5, 1])
# 设置坐标轴 到中心
ax = plt.gca()
ax.spines["top"].set_color("none")  # 设置上轴颜色为 none
ax.spines["right"].set_color("none")  # 设置右轴颜色为 none
ax.spines["left"].set_position(("data", 0))  # 设置左轴位置到 0
ax.spines["bottom"].set_position(("data", 0))  # 设置下轴位置到 0
# 绘制曲线
plt.plot(x, y, linestyle="--", linewidth=3,
         color="red", alpha=0.5, label=r"$sin(x)$")
plt.plot(x, y2, linestyle="--", linewidth=3,
         color="blue", alpha=0.5, label=r"$y=\frac{1}{2} cos(x)$")

# 绘制特殊点
xarray = [np.pi/2, np.pi/2]
yarray = [0, 1]
plt.scatter(xarray, yarray,
            marker='o',    # 点型
            s=60,          # 大小
            color='r',     # 颜色
            label="Points",
            zorder=3
)
# 为某个点添加备注
plt.annotate(r"$[\frac{\pi}{2}, 1]$",
             xycoords="data",
             xy=(np.pi/2, 1),
             textcoords="offset points",
             xytext=(30, 20),
             fontsize=14,
             arrowprops=dict(arrowstyle='-|>',
                             connectionstyle='angle3'
             )
)
plt.annotate(r"$[\frac{\pi}{2}, 0]$",
             xycoords="data",
             xy=(np.pi/2, 0),
             textcoords="offset points",
             xytext=(30, 20),
             fontsize=14,
             arrowprops=dict(arrowstyle='-|>',
                             connectionstyle='angle3'
             )
)
# 显示图例，前提是在plt.plot中加入label参数
plt.legend()

plt.show()

# 绘制水平线和垂直线
# 绘制垂直线
# plt.vlines([2,3,4], [2,4,2], 10)
# 绘制水平线
# plt.hlines(2, 1, 10)
# plt.show()
