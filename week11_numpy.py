import numpy as np

d2_33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(d2_33 > 5)
print(d2_33[d2_33 > 5])
print(d2_33[:, 2])
print(d2_33[:, 2] > 5)
print(d2_33[:] % 2 == 0)
print(d2_33[d2_33[:] % 2 == 0])
q = np.array([['a','b','c','d'],['c','c','g','h']])
matrix_a = np.array([[10, 20, 30], [10, 20, 30]])
matrix_b = np.array([[2, 2, 2], [1, 2, 3]])

# print(q[q =='c'])
# print(matrix_a - matrix_b)
# print(matrix_a + matrix_b)

print(matrix_a)
print(matrix_b)
print(matrix_a * matrix_b)