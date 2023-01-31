import numpy as np
from get_data import *

# A = np.array([1, 2, 3])

A=get_data_A("test_results/DS_MatrixA.txt")
temp=A[0]

pad_rows = 1
pad_cols = 2

# Use the numpy pad function to add rows and columns of zeroes to the matrix
padded_matrix = np.pad(temp, [(pad_rows, pad_rows), (pad_cols, pad_cols)], mode='constant')

temp2=np.shape(temp)
print("size",type(temp2),temp)
print(temp)


print(padded_matrix)
print("size",np.shape(padded_matrix))



