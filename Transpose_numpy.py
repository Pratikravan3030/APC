# Transpose operation on NumPy arrays
import numpy as np  

# Creating a 2D array
arr = np.array([[1, 2], [3, 4], [5, 6]])  

print('Our array is:')  
print(arr)  

print('\nAfter applying transpose function:')  
print(np.transpose(arr))   # or arr.T

# Creating another 2D array
arr2 = np.array([[7, 8, 9], [10, 11, 12]])  

print('\nThe second array is:')  
print(arr2)  

print('\nAfter applying transpose function:')  
print(np.transpose(arr2))   # or arr2.T
