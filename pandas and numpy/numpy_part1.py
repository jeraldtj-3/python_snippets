#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:59:57 2021
@author: thomas
"""

import numpy as np 
# import array 

# setting seed 
np.random.seed(121)

'''
videos, images, sounds, etc. 
''' 
# ndarray
type(np.array([8,2,3,2])) 


np.array([2,13,1,49])

# upcasting higher order data 
# one dimensional array 
np.array([2,4,'thomas'], )

# giving a special datatype 
np.array([2,3,1.3], dtype = 'float32') 

# two dimensional array 
np.array([[1,2,3], [23,12,44],[2324,1233,1231]])

# three dimensional array 
np.array([
    [[13,231,2],[23,12,42]], 
    [[23,12,3], [13,4,2]]
    ]) 

np.array([[1,2], [1,4], [32,42,1]])
# passing ndim paramter 
np.array([1,2,3], ndmin = 2) 

# dtype 
np.array([1.2, 32,3], dtype = 'complex') 

# passing tuples 
np.array([(1,3) , (3,12)]) 

# customising the dtypes 
arr = np.array([(1,3), (3,5)], dtype = [("a", 'int16'), ("b", "int8")])

type(arr[0][0])
type(arr[0][1]) 

type(arr[1][0])
type(arr[0][1]) 


# accessing the data 
arr = np.array([[12,34,2], [23,10,4],[3,2,3],[495,3,9]])

print(arr)
arr[0][1]

# default type is int64 
type(arr[0][1])

# matrices 
mat = np.mat(arr)# the type is matrix : but the representation is same 

# can use either mat or matrix 


# converting list into array 
l = [2,3,2,3,2,5,3,6,4] 
np.array(l)  # array()

np.asarray(l)  # asarray()

np.asanyarray(l) # ananyarray()

# matrix is already a type of array so it will not do any kind of array
np.asanyarray(mat)

# here the asarray convert matrix into array 
np.asarray(mat)


# matrix is subclass of array 
issubclass(np.matrix, np.ndarray)
issubclass(np.ndarray, np.matrix)
 

# deep copy and shallow copy 
a = arr # assign value of arr to a : shallow copy 

b = np.copy(arr)  # using copy : deep copy 

arr[0][0] = 123
print(arr)
print(a)   
print(b)  # holding old value 

'''
observations :
    * array are mutable 
    * deep copy and shallow copy 
''' 


# indexing and slicing 
#=============================================
for i in arr:
    print(i)

bools = np.fromfunction(lambda i , j : i ==j, (3,4)) 
arr1 = np.fromfunction(lambda i , j : i*j, (3,4)) 
print(arr1)

arr2 = np.fromfunction(lambda i , j : i/j, (3,4)) 
print(arr2) 
# inf keyword exists in numpy 
# otherwise we will get exception : zerodivision error 




# fromiterator 
# range is also a generator.  

gen = (i*i for i in range(5))  # generator object 

def test(x):
    yield x  
test(5) 


np.fromiter(gen, dtype = int)
np.fromiter(range(4), dtype = int)


# fromstring functtion 
np.fromstring('1,2,3,1,3,3,6,3,52', sep = ', ', dtype = 'int32')




# understanding ndim, size, shape, dtype  
# -------------------------------------------
arr1 = np.array([1,2,3,2,4,2,4]) 
arr2 = np.array([[2,1,3,3], [27,32,42,2]])

type(arr2)       
print(arr2.ndim)   # dimension 
print(arr2.size)   # no.of elements 
print(arr2.shape)   # shape 
print(arr2.dtype)  # type of elements 


# creating another three dimensional data 
arr_3 = np.array([
    [[1,2,3,2], [3,2,5,7],[2,2,4,3]],
    [[2,3,3,2], [34,3,3,9],[23,23,12,4]]
    ])
# two no of elements which has (3,4) dimension 

print(arr_3.shape) # elements_outside, elements_inside, values inside 
print(arr_3.size)
print(arr_3.ndim)




arr_3 = np.array([
    [
     [[1,2,3,2], [3,2,5,7],[2,2,4,3]],
     [[2,3,3,2], [34,3,3,9],[23,23,12,4]]
     ],
    [
     [[2,3,2,4], [3,2,54,46],[3,2,6,7]],
     [[3,2,764,4],[8,4,6,5],[5,6,5,5]]
     ]
    ])
# two no of elements which has (3,4) dimension 

print(arr_3.shape) # elements_outside, elements_inside, values inside 
print(arr_3.size)
print(arr_3.ndim)


# arange function in numpy 
r_array = np.arange(3.3,8,.2) 
print(r_array)

arr4 = np.arange(1,9)
print(arr4)

arr5 = np.arange(3.9)
print(arr5)


# linspace function 
lin = np.linspace(1,2,9) # getting equal distances 9 points between 1 and 2
print(lin)


# np.zeros funciton 
zeros = np.zeros((2,3,2,3)) 
print(zeros)

# np.one function 
ones = np.ones((3,2,3))
print(ones)


twos = np.ones((2,3,2))*2 
print(twos)


# empty function 
empty = np.empty((3,3))
print(empty)

# np.eyes() 
identity = np.eye(4)
print(identity)

np.linspace(2,4,4, endpoint = False, axis = 0) 
# axis = 0 for row 

np.linspace([2,3,4],4,4, endpoint = True, axis =1)


# logspace : evenly spaces but in log scale 
np.logspace(2,3,36)


# changing the dimension of the data 

d = np.linspace(1,200, 40)
print(d)
print(d.ndim)
print(d.shape)

# transposing 
d.reshape(40,1)
d.reshape(1,2,20)


d.reshape(2,4,5)


# ------------------------------
# np.random function 

# np.random.rand
rand_data = np.random.rand(3) # unifrom distribution  [0,1))

np.random.randn(5)  # from standard normal distribution 


ar = np.random.randn(2,2,3)

# randint function 
int_data = np.random.randint(1,4)
print(int_data)

# between 3 and 49 and  with (10,5) shape 
d1 = np.random.randint(3,49, (10,5))
print(d1)

# second number doesnt matter here
arr = np.array([[1,2,3,4,5,6],[12,1,2,1,2,1]]) 
arr.reshape(1,-3234)

#---------------------------------------------------
arr = np.random.randint(4,100,(5,5)) 
print(arr) 

print(arr[3:, 3:]) # subseting intersession 

# all rows, and (1,3) columns 
print(arr[:, [1,3]])

# boolean filtering 
print(arr>50) # boolean output 

# get those elements 
print(arr[arr>50])



# multiplication : not exact matrix multiplication
arr1 = np.random.randint(2,4,(3,3))
arr2 = np.random.randint(3,5,(3,3)) 

print(arr1*arr2)


# mathematical matrix multiplication 
print(arr1@arr2)


# columnwise and rowwise broadcasting 
# addition  : broadcasting :  
ar1 = np.array([1,2,3,4,3]) 
ar2 = np.random.randint(2,6,(5,4)) 

# column wise broadcasting 
ar2+ar1.reshape(5,1)


# row wise addition 
b = np.array([1,1,1,1]) 
print(ar2+b) 

# other operations 

print(arr1)
print(np.sqrt(arr1))

print(np.exp(arr1) )
print(np.log10(arr1))

print(np.log2(arr1))




np.random.seed(30)
np.random.rand(2,4)

















