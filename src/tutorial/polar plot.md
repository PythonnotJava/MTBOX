```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
theta = np.linspace(0, 2*np.pi, 100)
r = np.random.rand(100)

# 绘制极坐标图
plt.polar(theta, r)

# 添加标题
plt.title('Example Polar Plot')

# 显示图形
plt.show()

```