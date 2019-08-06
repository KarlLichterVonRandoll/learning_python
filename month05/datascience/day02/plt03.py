import matplotlib.pyplot as plt

# 绘制子图
# 矩阵式布局
plt.figure('subplot layout',
           facecolor='lightgray')
# 拆分矩阵
# 显示九宫格
for i in range(9):
    # 操作 3*3 矩阵的第i+1个子图
    plt.subplot(3, 3, i + 1)
    plt.text(0.5, 0.5, i,
             ha='center',
             va='center',
             size=37,
             alpha=0.7)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

plt.show()
