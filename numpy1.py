import numpy as np
arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 6, 5, 4], 
                [2, 12, 23, 10, 60]])
print(arr)
print("element in the row",arr[1:3])
# import numpy as np
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 6, 5, 4], [2, 12, 23, 10, 60]])  # All rows have the same length
# print(arr)
# print("Elements in the row range:", arr[1:3])

# import numpy as np
arr = np.array([[[1,2,3], [4,5,6]], [[7,6,5], [6,7,5]]])
print(arr)
print(arr[1,0,2]) #arr[matrix,row,column]
#negative indexing
print(arr[-1,-1,-1])

# import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,90])
print(arr[1:2:4])

#splitting array
# import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)
print(newarr)
print(newarr[0])