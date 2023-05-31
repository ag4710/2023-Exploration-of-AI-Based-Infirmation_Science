import numpy as np

d2_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# list style
print(d2_array[2][0], d2_array[-1][-3], d2_array[2][-3])
# numpy style
print(d2_array[2, -3], d2_array[-1, 0])
d2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(d2)

d2_array[0, 0] = 11
print(d2_array)
print(d2[::2][::2])  # 첫 슬라이싱 : 0행, 2행 선택 후 /// 두 번째 슬라이싱: 그 중 0행 선택
print(d2[::2, ::2])  # 행 슬라이싱 : 0행, 2행 선택 /// 열 슬라이싱 : 0열, 2열 선택

d2_array[0, 0] = 22.71  # truncation
print(d2_array)
print(d2[0:2, 2:])
print(d2[1], d2[1,:])
print(d2[:, 2:3])
print(d2[:, 2])
print(d2[0:2, 0:2])
print(d2[1::2, 1::2])