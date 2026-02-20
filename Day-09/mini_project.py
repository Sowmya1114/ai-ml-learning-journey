import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print("Row Sum: ",np.sum(arr,axis=1))
print("Column Sum: ",np.sum(arr,axis=0))
print("Total Sum: ",np.sum(arr))
print("Max: ",np.max(arr))
print("Min: ",np.min(arr))
