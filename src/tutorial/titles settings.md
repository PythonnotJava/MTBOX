```python
import matplotlib.pyplot as plt
import numpy as np


# 创建数据
x = np.linspace(0, 10, 100)
y = x ** 2

# 创建图像和子图
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# 绘制子图并设置标题
axs[0, 0].plot(x, y, label='y=x^2')
axs[0, 0].set_title('Plot 1', fontsize=16)
axs[0, 1].plot(x, np.sin(x), label='y=sin(x)')
axs[0, 1].set_title('Plot 2', fontsize=16)
axs[1, 0].plot(x, np.cos(x), label='y=cos(x)')
axs[1, 0].set_title('Plot 3', fontsize=16)
axs[1, 1].plot(x, np.tan(x), label='y=tan(x)')
axs[1, 1].set_title('Plot 4', fontsize=16)

# 设置主标题和副标题
fig.suptitle('Multiple Subplots Example', fontsize=24, color='navy')
fig.text(0.5, 0.92, 'This is the main title', ha='center', fontsize=18, color='gray')
fig.text(0.5, 0.05, 'This is the x axis label', ha='center', fontsize=14, color='gray')
fig.text(0.05, 0.5, 'This is the y axis label', va='center', rotation='vertical', fontsize=14, color='gray')

# 显示图像
plt.show()

```