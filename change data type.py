#convert the value are data type of the array
import numpy as np
x=np.array([1,2,3,4],dtype="f")
print("data type : ",x.dtype)
#another mathod to convert 
num1=np.array([1,2,3,4])
x2=np.float64(num1)
print("data type :",num1.dtype)
print("data type :",x2.dtype)

