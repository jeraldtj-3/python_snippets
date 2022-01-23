

# the difference between arguments and parameters 
# positional and keyword arguments 
# default arguments 
# variable-length arguments (*args and **kwargs) 
# container unpacking into function arguments 
# local vs. global arguments 
# parameter passing (by value or by reference) 

def print_name(name):
    print(f'hi {name}') 

# function parameters are the names listed in the function's definition.
# function arguments ar the real values passed to the function 

# print_name('thomas') # thomas is the argument 

def customer_info(email, phone_number,name = 'Thomas'):  # default name is thomas
    print(f"{name}'s email is {email} and the phone number is {phone_number}") 

# customer_info('thomasreji155@gmail.com',9562348628,name = 'thomaskutty')

def sum_(*args):
    for i in args:
        print(i) 

# sum_(2,4,2,4,'thomas')


def keys(**kwargs):
    for i in kwargs.items(): # tuple of (key,value)
        print(i) 


keys(name= 'thomas',age = 25)

