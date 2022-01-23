

# functions in python are first-class objects 
# created at runtime 
# assigned to a variable or lement in a data structure 
# passed as an argument to a function 
# returned as the result of a function
# integers, strings and dictionaries are other examples of first-class objects in python

# treating a function like objects 
def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1) 

print(factorial(3))
# get the documentation of the function 
# __doc__ is one of the several attributes of function objects 
print(factorial.__doc__)  # returns the n! 

# factorial is an instance of the function class 
print(type(factorial)) # belongs to the function class 

# storing the factorial function into a variable 
fact = factorial

print(factorial) 
print(fact)
print(fact(8)) 

fact_map_object = map(fact,range(1,10))
print(fact_map_object) 
print(list(fact_map_object)) 

















