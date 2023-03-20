```python
import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体
plt.rcParams.update({'font.family': 'serif', 'font.size': 14})

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# 创建图像和子图，并设置画布颜色和背景颜色
fig, axs = plt.subplots(3, 1, figsize=(8, 10))
fig.patch.set_facecolor('lightgray')
axs[0].set_facecolor('white')
axs[1].set_facecolor('white')
axs[2].set_facecolor('white')

# 绘制曲线并设置颜色
axs[0].plot(x, y1, color='red', label='sin(x)')
axs[1].plot(x, y2, color='green', label='cos(x)')
axs[2].plot(x, y3, color='blue', label='tan(x)')

# 添加标签和标题
axs[0].set_xlabel('x', color='darkgray')
axs[0].set_ylabel('y', color='darkgray')
axs[0].set_title('Sine Function', color='black')

axs[1].set_xlabel('x', color='darkgray')
axs[1].set_ylabel('y', color='darkgray')
axs[1].set_title('Cosine Function', color='black')

axs[2].set_xlabel('x', color='darkgray')
axs[2].set_ylabel('y', color='darkgray')
axs[2].set_title('Tangent Function', color='black')

# 设置坐标轴和网格线样式
for ax in axs:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.xaxis.set_tick_params(width=1.5, color='darkgray')
    ax.yaxis.set_tick_params(width=1.5, color='darkgray')
    ax.grid(color='gray', linestyle='--', alpha=0.5)

# 设置图例样式和字体颜色
for ax in axs:
    legend = ax.legend(loc='upper right', fontsize=12)
    for line in legend.get_lines():
        line.set_linewidth(3.0)
    for text in legend.get_texts():
        text.set_color('darkgray')

# 显示图像
plt.show()

```