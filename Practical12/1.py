print("By 22IT460")
import numpy as np
arr1 = eval(input("Enter the array: "))
arr1 = np.array(arr1)
min = np.min(arr1)
max = np.max(arr1)
print(f"min: {min}, max: {max} in the {arr1}")