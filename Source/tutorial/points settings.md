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

# 绘制点并设置样式
ax.scatter(2, 4, s=80, c='red', marker='*', alpha=0.8, label='point A')
ax.scatter(8, 64, s=120, c='green', marker='o', alpha=0.6, label='point B')

# 设置图例样式
ax.legend(loc='upper left', fontsize=14, frameon=True, edgecolor='darkgray')

# 显示图像
plt.show()

```