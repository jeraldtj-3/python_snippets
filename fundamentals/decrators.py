
def outer_function(msg): # outer function 
	def inner_function():  # inner function 
		print(msg)     # access to the inner variable 
	return inner_function  # inner function 


def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		print('wrapper executed this before {}.'.format(original_function.__name__))
		original_function()
	return wrapper_function 

@decorator_function 
def display():
	print('display function ran')


@decorator_function
def display_info(name,age):
	print('display_info ran with arguments ({},{})'.format(name,age))


display()
display_info('john',25)



sudo pip install h5py 
model.save_weights('model_name.h5')

