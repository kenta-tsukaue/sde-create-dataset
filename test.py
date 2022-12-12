import numpy as np
"""基本の画像の行列を作成"""
standard_vector = []
for i in range(32):
    standard_vector.append(0)
standard_matrix = []
for i in range(32):
    standard_matrix.append(standard_vector)
standard_tensor = []
for i in range(10):
    standard_tensor.append(standard_matrix)

#print("standard_tensor[0]: ", standard_tensor[0])

standard_tensor = np.array(standard_tensor)
standard_tensor = np.transpose(standard_tensor, (1, 2, 0))
print(standard_tensor.shape)