```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.normal(0, 1, 1000)

# 绘制直方图
plt.hist(data, bins=30, density=True, alpha=0.5)

# 添加标题和标签
plt.title('Example Histogram')
plt.xlabel('Values')
plt.ylabel('Density')

# 显示图形
plt.show()
```
