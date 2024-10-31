import numpy as np

# part 1
arr1 = np.arange(1, 11)
sum_ = np.sum(arr1)
mean_ = np.mean(arr1)
prod_ = np.prod(arr1)

print(f"Sum: {sum_}\nMean: {mean_}\nProduct: {prod_}\n\n")

# part 2
arr2 = np.random.randint(1, 11, size=(3, 3))
trans = np.transpose(arr2)
print("Transpose: \n", trans)

# part 3
arr3 = np.arange(1, 21)
arr3 = arr3.reshape(4, 5)
print("\n\nReshaped array\n", arr3)

# part 4
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
arr4 = np.array(l1)
arr4_ = np.array(l2)

summ = arr4 + arr4_
diff = arr4_ - arr4
mul = arr4 * arr4_
div = arr4 / arr4_
print(
    f"\n\nResult of Addition: {summ}\nResult of Subtraction: {diff}\nResult of Multiplication: {mul}\nResult of Division: {div}\n\n")

# part 5
# using arr1 array in first part containing 10 elements
sq_ = np.sqrt(arr1)
print(f"Result of Squaring elements of array:\n{sq_}\n\n")

# part 6
arr6 = np.arange(1, 5).reshape(2, 2)
det_ = np.linalg.det(arr6)
inv_ = np.linalg.inv(arr6)
print(f"Determinant: {det_}\nInverse:\n{inv_}\n\n")

# part 7
arr7 = np.random.random(50)
index_max = np.argmax(arr7)
index_min = np.argmin(arr7)
print(f"Index with max element: {index_max}\nIndex with min element: {index_min}\n\n")

# part 8
arr8 = np.array([[1, 2, 3], [1, 1, 4], [3, 4, 0]])  # 3x3 coff matrix
arr8_const = np.array([4, 7, 9])  # 3x1 matrix for constants
sol = np.linalg.solve(arr8, arr8_const)
print(f"Solution of Linear Equation:\n{sol}\n\n")

# part 9
arr9 = np.arange(1, 26)
per = np.percentile(arr9, 75)
print(f"75th Percentile: {per}\n\n")


# part 10
def func(arr):
    mean__ = np.mean(arr)
    dev = np.std(arr)
    nor = (arr - mean__) / dev
    return nor


arr10 = np.arange(1, 11)
# nor_arr=np.frompyfunc(func,1,1)
nor_arr = func(arr10)
print(f"Normalized array: \n{nor_arr}\n")
