import matplotlib.pyplot as plt
import matplotlib.gridspec as mg

# 绘制子图
# 网格式布局，支持单元格合并
plt.figure("Grid layout", facecolor="lightgray")

# 使用GridSpec方法拆分网格式布局
gs = mg.GridSpec(3, 3)
# 合并0行的前两列为一个单元格
plt.subplot(gs[0, :2])
plt.text(0.5,0.5,'1', ha='center', va='center',size=36, alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[:2, 2])
plt.text(0.5,0.5,'2', ha='center', va='center',size=36, alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1, 1])
plt.text(0.5,0.5,'3', ha='center', va='center',size=36, alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1:, 0])
plt.text(0.5,0.5,'4', ha='center', va='center',size=36, alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[2, 1:])
plt.text(0.5,0.5,'5', ha='center', va='center',size=36, alpha=0.7)
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
