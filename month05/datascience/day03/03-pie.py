import numpy as np
import matplotlib.pyplot as plt

# 绘制饼图
labels = ['Python', 'Javascript', 'C++',
          'Java', 'PHP']
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']

plt.figure("Pie", facecolor="lightgray")
plt.title("Pie")

plt.axis('equal')  # 等轴比例显示正圆
plt.pie(values,  # 值列表
        spaces,  # 扇形区域之间的间距列表
        labels,  # 标签列表
        colors,  # 颜色列表
        '%.1f%%',  # 标签所占比例格式
        shadow=True,  # 是否显示阴影
        startangle=45,  # 逆时针绘制饼状图时的起始角度
        radius=1)  # 半径

plt.legend()
plt.show()
