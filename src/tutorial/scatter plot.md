```python
import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
mean = 0
std = 1
num_samples = 1000
x = np.random.normal(mean, std, num_samples)
y = np.random.normal(mean, std, num_samples)

# 绘制散点图
plt.scatter(x, y, alpha=0.5)

# 添加标题和标签
plt.title('Normal Distribution Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```