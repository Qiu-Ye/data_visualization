"""绘制散点图"""

import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor = 'none', s=2)

"""颜色映射"""
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor = 'none', s=2)

"""设置图表标题，并给坐标轴加上标签"""
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

"""设置刻度标记的大小"""
plt.tick_params(axis='both', which='major', labelsize=14)

"""显示图表"""
plt.show()

"""自动保存图表"""
# plt.savefig('squares_plot.png', bbox_inches='tight')