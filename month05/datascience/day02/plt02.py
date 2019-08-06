import numpy as np
import matplotlib.pyplot as plt

# 手动构建 matplotlib 窗口
plt.figure("figure01",      # 窗口标题
           figsize=(4, 3),  # 窗口大小
           dpi=120,         # 像素大小
           facecolor='lightgray')   # 背景颜色
plt.title("title1", fontsize=14)  # 设置图表标题
plt.grid(linestyle=':')  # 设置网格线
plt.xlabel("time", fontsize=12)  # 设置水平轴文本
plt.ylabel("price", fontsize=12)  # 设置垂直轴文本
plt.tick_params(labelsize=8)  # 设置刻度字体大小
plt.tight_layout()  # 紧凑图表布局
plt.figure("figure02",      # 窗口标题
           figsize=(4, 3),  # 窗口大小
           dpi=120,         # 像素大小
           facecolor='lightgreen')   # 背景颜色
plt.show()
