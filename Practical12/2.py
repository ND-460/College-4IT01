print("By 22IT460")
import numpy as np
arr1 = np.array(eval(input("Enter the array1: ")), dtype=int)
arr2 = np.array(eval(input("Enter the array2: ")), dtype=int)
common_items = np.intersect1d(arr1, arr2)
print(f"common_items: {common_items} in {arr1} and {arr2}")