import numpy as np
# Create an Numpy array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
sec = np.array([[4,5,6],[1,2,3],[7,8,9]])
print("Numpy array :")
# Calculate the sum of arrays
print("Sum of the arrays")
print(np.add(arr , sec))
print("Multiply the arrays")
print(np.multiply(arr , sec))
print("mean of the arrays")
print(np.mean(arr))
print(np.mean(sec))
print("Standard Deviation of arrays")
std_dev = np.std(arr)
print(std_dev)
 