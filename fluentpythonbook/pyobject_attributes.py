class c:
	pass 

obj = c()

def func():
	pass 

#  listing attributes of functions that don't exist in plain instances
specific_func_attributes = sorted(set(dir(func)) - set(dir(obj)))
print(specific_func_attributes)

# __annotations__ >> dict >> parameter and return annotations 
# __call__ >> method-wrapper >> implementation of the () operator, the callable protocol 
# __closure__ >> tuple >> the function closure, ie binding for free variables 
# __code__ >> code >> function metadata and function body compiled into bytecode 
# __defaults__ >> tuple >> default values for the formal paramters 
# __get__ >> method-wrapper >> implementation of the read-only descriptor protocol 
# __globals__ >> dict >> global variables of the module where th efunctio is defined 
# __kwdefaults__ >> dict >> default values for the keyword-only formal paramters 
# __name__ >> str >> the function name 
# __qualname__ >> str >> the qualified function name




