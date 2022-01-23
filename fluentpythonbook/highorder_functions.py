# Higher order func: function that takes a function as argument or returns a function as a result 
# ex. map, sorted,filter 

fruits = ['strawberry','fig','apple','cherry','respberry','banana'] 
sorted_fruits = sorted(fruits, key = len)
print(sorted_fruits)

def reverse(word):
	return word[::-1]

sorted_reverse = sorted(fruits,key = reverse)
print(sorted_reverse)

def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1) 
# using list comprehension 
factorials = [factorial(i) for i in range(1,10)] 
print(factorials) 

filter_output = list(map(factorial,filter(lambda x : x%2, range(1,6))))
print(filter_output) 


filter_output2 = [factorial(n) for n in range(1,6) if n%2]
print(filter_output2)

from functools import reduce 
from operator import add
sum_ = reduce(add,range(100)) 
print(sum_) 

sum_2 = sum(range(100))
print(sum_2)

# userdefined functions created with def  statements or lambda expressions. 
# built in functions: implemented in c like len, time.strftime. 
# built in methods : methods implemented in C, like dict.get 
# methods: functions defined in the body of a class.
# classes: when invoked a class runs its __new__ methodd to create an instance 
# then __init__ to initialize it, and finally the instance is returned to the 
# caller. Because there is no new operator in pytohn,calling a class is like callign a afunction 

# class instances : if a class defines a __call__ method, then its instances may be invoked as functions.

# generator functions: functions or methods that use the yield keyword. When called,generator functions return a generator object 


print(abs, str,19) 


