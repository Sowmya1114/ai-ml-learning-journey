import numpy as np
a=np.array([1,9,16])
b=np.array([3,4,5])
print("Addition: ",a+b)
print("Multiplication: ",a*b)
print("Subtraction: ",a-b)
print("Division: ",a/b)
print("Square root of a: ",np.sqrt(a))
print("Power of b: ",np.power(a,b))

#shape and Reshape
arr=np.array([[1,2,3],[4,5,6]])
print("Shaped: ",arr.shape)
reshaped=arr.reshape(3,2)
print("Reshaped: ",reshaped.shape)

#Indexing and Slicing
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[1])
print(arr[0:3])

mat=np.array([[1,2,3],[4,5,6]])
print(mat[0,1])
print(mat[0:])
print(mat[-1:])
