import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=16)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# 设置刻度标记的样式
ax.tick_params(labelsize=12)

plt.show()
