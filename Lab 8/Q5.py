import numpy as np

arr1 = np.random.choice([2,5,9,10],size = (4,4))
print(f"{arr1}\n")
arr2=np.arange(1,32,2).reshape(4,4)

new_arr=arr1*np.identity(4)
print(f"{new_arr}\n")
sum_arr=np.add(arr2,new_arr)
print(f"{sum_arr}\n")
