import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

# creating array from list
a = [1, 2, 3, 4, 5]
print(type(a))
arr = np.array(a)
print(type(arr))
print(arr)

#mixed element array
a = [2.5, 3.5, 7, 4.5, 8]
arr = np.array(a)
print(arr)

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[9,12,13]]
print('List of List = ', a)
print()

arr = np.array(a)
print(arr)

a = [1, 2, 3, 4, 5]
arr = np.array(a)

print('Original Array      = ', arr)
print('Add 5 to Array      = ', arr + 5)
print('Multiply arr with 2 = ', arr * 2)
