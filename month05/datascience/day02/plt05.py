import matplotlib.pyplot as plt
import matplotlib.gridspec as mg
import numpy as np

# 绘制子图
# 自由式布局
# plt.figure("Flow layout", facecolor="lightgray")

# 设置图表位置，包括左下角点x左边，y坐标，宽度，高度 数值表示百分比
# plt.axes([0.1, 0.2, 0.5, 0.5])
# plt.text(0.5,0.5,'1', ha='center', va='center',size=36, alpha=0.7)

# locators = ['plt.NullLocator()',
#             'plt.MultipleLocator(2)',
#             'plt.MaxNLocator(nbins=3)',
#             'plt.AutoLocator()']

# 刻度定位器
# plt.figure("locator", facecolor="lightgray")
# for i, locator in enumerate(locators):
#     plt.subplot(len(locators), 1, i+1)
#     # 获取当前坐标轴
#     ax = plt.gca()
#     # 隐藏除底轴之外的所有坐标轴
#     ax.spines['left'].set_color("none")
#     ax.spines['right'].set_color("none")
#     ax.spines['top'].set_color("none")
#     plt.xlim(1, 10)
#     plt.ylim(-1, 1)
#     # plt.yticks([])  # 去除y轴刻度
#     ax.spines['bottom'].set_position(('data', 0))
#     # 设置水平坐标轴的主刻度定位器
#     ax.xaxis.set_major_locator(eval(locator))
#     # 设置水平坐标轴的次刻度定位器
#     ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
#     plt.text(5, 0.3, locator, ha='center', size=12)


# 刻度网格线
y = np.array([1,10,100,1000,100,10,1])
plt.figure('Normal & log', facecolor='lightgray')
plt.subplot(211)
plt.title('Normal', fontsize=20)
plt.ylabel('y', fontsize=14)
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
# 绘制刻度网格线
ax.grid(which='major',
        axis='both',
        linewidth=1,
        linestyle='-',
        color='r',
        alpha=0.5)
ax.grid(which='minor',
        axis='both',
        linewidth=1,
        linestyle='-',
        color='orange',
        alpha=0.5)
plt.plot(y, 'o-', c='dodgerblue', label='plot')
plt.legend()

# 第二张半对数坐标
plt.subplot(212)
plt.title('Normal', fontsize=20)
plt.ylabel('y', fontsize=14)
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
# 绘制刻度网格线
ax.grid(which='major',
        axis='both',
        linewidth=1,
        linestyle='-',
        color='r',
        alpha=0.5)
ax.grid(which='minor',
        axis='both',
        linewidth=1,
        linestyle='-',
        color='orange',
        alpha=0.5)
plt.semilogy(y, 'o-', c='dodgerblue', label='plot')
plt.legend()

plt.show()
