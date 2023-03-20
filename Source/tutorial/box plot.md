```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
data = np.random.normal(0, 1, 100)

# 绘制箱线图
plt.boxplot(data)

# 添加标题和标签
plt.title('Example Box Plot')
plt.xlabel('Data')

# 显示图形
plt.show()

```