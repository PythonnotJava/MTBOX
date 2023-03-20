```python
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = x ** 2

# 创建图像和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制曲线并设置标签
ax.plot(x, y, label='y=x^2')

# 设置x轴和y轴标签样式
ax.set_xlabel('x', fontsize=16, fontweight='bold', color='darkgray')
ax.set_ylabel('y', fontsize=16, fontweight='bold', color='darkgray')

# 设置标题
ax.set_title('Parabola', fontsize=20, fontweight='bold', color='darkgray')

# 设置x轴和y轴标签的位置
ax.xaxis.set_label_coords(0.95, -0.05)
ax.yaxis.set_label_coords(-0.05, 0.95)

# 设置x轴和y轴标签的旋转角度
ax.xaxis.label.set_rotation(0)
ax.yaxis.label.set_rotation(90)

# 设置x轴和y轴标签的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置x轴和y轴刻度线样式
ax.tick_params(axis='both', which='major', length=10, width=1.5, color='darkgray', direction='inout')
ax.tick_params(axis='both', which='minor', length=5, width=1, color='gray', direction='inout')

# 设置坐标轴和网格线样式
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.xaxis.set_tick_params(width=1.5, color='darkgray')
ax.yaxis.set_tick_params(width=1.5, color='darkgray')
ax.grid(color='gray', linestyle='--', alpha=0.5)

# 设置图例样式
ax.legend(loc='upper left', fontsize=14, frameon=True, edgecolor='darkgray')

# 显示图像
plt.show()

```