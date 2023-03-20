```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.rand(10, 10)

# 绘制热力图
plt.imshow(data, cmap='hot', interpolation='nearest')

# 添加颜色条
plt.colorbar()

# 显示图形
plt.show()

```