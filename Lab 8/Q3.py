import numpy as np

arr1= np.arange(2,19,2).reshape(3,3)
print(f"{arr1}\n")
arr2=4*arr1
print(f"{arr2}\n")
arr3=arr2*np.identity(3)
print(f"{arr3}\n")
