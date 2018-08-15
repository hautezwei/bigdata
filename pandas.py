import py_compile

import numpy as np

py_compile.compile(r'pandas.py')

print("activity")
print("activity")
print("activity")
print("activity")
print("activity")

arr1 = np.arange(10)

print(arr1)

print(type(arr1))

arr2 = np.array(np.arange(12)).reshape(4, 3)

print(arr2)

print(type(arr2))

dic2 = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12], 'd': [13, 14, 15, 16]}
