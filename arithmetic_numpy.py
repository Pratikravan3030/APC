import numpy as np  

# First array
arr1 = np.array([[1, 2], [3, 4]])  
print('First array:')  
print(arr1)  

# Second array
arr2 = np.array([[5, 6], [7, 8]])  
print('\nSecond array:')  
print(arr2)  

# Addition
print('\nAfter adding the two arrays:')  
print(np.add(arr1, arr2))  

# Subtraction
print('\nAfter subtracting the two arrays:')  
print(np.subtract(arr1, arr2))  

# Multiplication
print('\nAfter multiplying the two arrays:')  
print(np.multiply(arr1, arr2))  

# Division
print('\nAfter dividing the two arrays:')  
print(np.divide(arr1, arr2))  
