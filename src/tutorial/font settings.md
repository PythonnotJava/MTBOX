```python
import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 14,
    'font.weight': 'bold',
    'axes.labelweight': 'bold',
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

# 创建数据
x = np.linspace(0, 10, 100)
y = x ** 2

# 创建图像和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制曲线并设置颜色
ax.plot(x, y, color='red', label=r'$y=x^2$')

# 添加标签和标题
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Parabola')

# 添加箭头指向函数名
arrow_x = 5
arrow_y = arrow_x ** 2
arrow_text = r'$y=x^2$'
ax.annotate(arrow_text, xy=(arrow_x, arrow_y), xytext=(arrow_x - 2, arrow_y + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=16)

# 设置坐标轴和网格线样式
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, color='darkgray')
ax.yaxis.set_tick_params(width=1.5, color='darkgray')
ax.grid(color='gray', linestyle='--', alpha=0.5)

# 设置图例样式和字体颜色
legend = ax.legend(loc='upper left', fontsize=12)
for line in legend.get_lines():
    line.set_linewidth(3.0)
for text in legend.get_texts():
    text.set_color('darkgray')

# 显示图像
plt.show()

```