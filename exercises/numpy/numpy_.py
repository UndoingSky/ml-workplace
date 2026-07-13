import numpy as np

array = np.array([1, 2, 3, 4]) #1D array
array_2n = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]) #2D array

array_3n = np.array([[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
                     [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
                     [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]])

print(array.ndim)
print(array_2n.ndim)

sum = array_3n[0, 0, 0] + array_3n[1, 2, 3]
print(sum)

slicing = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11 ,12],
                    [13, 14, 15,16]])

print(slicing[:2, 2:])


table1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
table2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(table1.shape)
print(table2.shape)

multiplication_table = table1 * table2

print(multiplication_table)



rng = np.random.default_rng()

print(rng.integers(0, 7))