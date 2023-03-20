```python
import matplotlib.pyplot as plt

# 准备数据
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 36, 40, 22]

# 绘制条形图
plt.bar(x, y)

# 添加标题和标签
plt.title('Example Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图形
plt.show()

```