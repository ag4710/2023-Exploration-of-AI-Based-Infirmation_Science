import numpy as np

# b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) + np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# b = np.array(range(1, 11)) + np.array(range(10, 101, 10))
b = np.arange(1, 11) + np.arange(10, 101, 10)
print(b, b.shape, b.size, b.ndim)
d2_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# list style
print(d2_array[2][0], d2_array[-1][-3], d2_array[2][-3])
# numpy style
print(d2_array[2, -3], d2_array[-1, 0])

scores = np.array([2500000, 2200000, 2300000])
# scores = scores + 50
# scores = scores * 3
scores = scores * 0.026 / 12.0
print(scores)
d2_array[0, 0] = 11
print(d2_array)

mixed = np.array([-9, 'ISHS', False, 2.71])
print(mixed)
d2_array[0, 0] = 22.71  # truncation
print(d2_array)