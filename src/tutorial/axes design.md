```python
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(-5, 5, 100)
y = x ** 2

# 创建图像和子图
fig, ax = plt.subplots()

# 绘制曲线
ax.plot(x, y, label='$y = x^2$')

# 设置x轴位置和样式
ax.spines['bottom'].set_position(('data', 0))
ax.spines['bottom'].set_color('gray')
ax.spines['bottom'].set_linewidth(1.5)
ax.set_xlabel('$x$')

# 设置y轴位置和样式
ax.spines['left'].set_position(('data', 0))
ax.spines['left'].set_color('gray')
ax.spines['left'].set_linewidth(1.5)
ax.set_ylabel('$y$')

# 添加网格线
ax.grid(True, linestyle='--', alpha=0.5)

# 添加标题和图例
ax.set_title('Quadratic Function', fontsize=16)
ax.legend()

# 显示图像
plt.show()

```