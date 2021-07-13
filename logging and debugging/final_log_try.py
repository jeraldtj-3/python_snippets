

import logging 

'''
logging levels 


DEBUG - Detailed information, typically of interest only when diagisingproblems 
INFO - Confirmation that things are working as expected. 
WARNING - An indication that something unexpected happend, or indicative
        of some problem in the near future.
ERROR - Due to more serious problem, the software has not been able to perorm some function 
CRITICAL - A serious error, indicating that the program itself may be unable to continue running. 


'''

def add(x,y):
    return x+y 

def substract (x, y):
    return x-y 

def divide(x,y):
    return x/y 

num_1 = 32
num_2 = 234 


add_result = add(num_1, num_2) 
substract_result = substract(num_1, num_2) 
divide_result = divide(num_1, num_2) 












