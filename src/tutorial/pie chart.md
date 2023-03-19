```python
import matplotlib.pyplot as plt

# 准备数据
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 5]

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 添加标题
plt.title('Example Pie Chart')

# 显示图形
plt.show()

```