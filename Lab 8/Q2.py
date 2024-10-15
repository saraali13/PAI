import numpy as np

arr1 = np.arange(1, 19, 9)
print(arr1)

arr2 = arr1.reshape(3, 3)
print(arr2)

for i in arr1:
    print(i)
