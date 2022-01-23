import random 

class BingoCage:
	def __init__(self,items):
		self._items = list(items)
		random.shuffle(self._items) 
	def pick(self):
		try:
			return self._items.pop() 
		except IndexError:
			raise LookupError('pick from empty BingoCage')
	# shortcut to bingo.pick():bingo() 
	def __call__(self):
		return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())

# __call__ : pick() will get executed 
print(bingo())

print(callable(bingo))

# a class implementing __call__ is an easy way to create function-like objects. 

def factorial(n):
    '''returns n!'''
    return 1 if n<2 else n*factorial(n-1) 


# function objects have many attributes beyond __doc__ 
attributes = dir(factorial)
import time 
print(attributes)
time.sleep(2)



