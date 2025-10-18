import numpy as np
print(np.__version__)

###print a list in numpy
array = np.array([1,2,3,4])
print(array)
print(type(array))
print(array.dtype)
print(array.ndim)

array2 =np.array([['A','B','C'],['A','B','C']])
print(array2.ndim)
print(array2.shape)

##multi-index indexing
print(array2[1,1])
array3= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array3[0,2])

## Math function
print(np.pi)
print(np.round(np.pi))

#Vectorized Math function
radii = np.array([1,2,3])
print(np.pi*radii*radii) #area of circle = pi*radii^2


#Element wise arithmetic
array4= np.array([1,2,3])
array5= np.array([4,5,6])

print(array4+array5)


#Comparison Operator
scores = np.array([100,98,87,89])
print(scores == 87)

scores[scores< 90 ]=0
print(scores)
