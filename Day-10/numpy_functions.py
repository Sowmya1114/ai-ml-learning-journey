import numpy as np
arr=np.array([4,9,2])
print("Square root: ",np.sqrt(arr))
print("Mean: ",np.mean(arr))
print("Normalization: ",np.std(arr))
print("Sum: ",np.sum(arr))
print("Max: ",np.max(arr))
print("Min: ",np.min(arr))


#numpy_random
import numpy as np
#randomness
print(np.random.rand(5))
print(np.random.randint(1,100,5))
#reproducibility
np.random.seed(42)
print(np.random.randint(1, 10))
print(np.random.randint(1, 10))

#broadcasting
import numpy as np
arr = np.array([1, 2, 3])
scalar = 5
print(arr + scalar)   

#2D example
mat = np.array([[1,2,3],
                [4,5,6]])
print(mat + 10)

#boolean masking
import numpy as np
arr = np.array([10, 25, 30, 15, 50])
print(arr[arr > 20])
print(arr[arr % 2 == 0])
