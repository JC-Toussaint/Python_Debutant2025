import numpy as np

x = np.array([[1,2], [4,5], [7, 8]])
y = np.array([[4,5], [1,2], [6, 2]])
print(x.shape)
print(20*'-')
print(y.shape)
print(np.cross(x, y))
