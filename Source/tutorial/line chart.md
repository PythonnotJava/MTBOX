```python
import numpy
import matplotlib.pyplot as plt

# y = x^2
x = numpy.linspace(-10, 10, 1000)
y = x ** 2

# y = (x-2)^2
x2 = numpy.linspace(-10, 10, 10)
y2 = (x2 - 2) ** 2

plt.figure(figsize=(12, 12))
plt.plot(x, y, x2, y2, lw=2)
plt.show()
```