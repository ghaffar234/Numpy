#make the programe to build the 1D ,2D and 3D array using the numpy
import numpy as np
x=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(x)
print(x.ndim)
# make program for make the n number of dimension of array 
x=np.array([1,2,3,4],ndmin=10)
print(x)
print(x.ndim)