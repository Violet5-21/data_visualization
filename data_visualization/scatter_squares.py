import matplotlib.pyplot as plt


x_values = range(1, 10001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=8)

# 设置图题并给坐标轴加上标签
ax.set_title('Square Numbers', fontsize=16)
ax.set_xlabel('Square Numbers', fontsize=12)
ax.set_ylabel('Square Numbers', fontsize=12)


# 设置刻度标记的样式
ax.tick_params(labelsize=12)

# 设置每个坐标值的取值范围
ax.axis([0, 1_100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png', bbox_inches='tight')
