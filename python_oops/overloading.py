

class multiplynumeric():
	def __init__(self,a):
		self.a = a 
	def __mul__(self,other):
		return self.a+other.a 

	def __add__(self,other):
		return self.a*other.a 

mul = multiplynumeric(7)
mul2 = multiplynumeric(8)

# multiplying the objects 
# mul*mul1 

print(mul.a * mul.a)

# operator overloading methods 
print(mul*mul2)
print(mul+mul2)


# stirng overloading 
# method overloading 



###############  POLYMORPHISM ########################### 

def test(a,b):
	return a+b 

# datatype is differnt but the the function is same 
print(test(3,4))   # addition 
print(test('thomas ', 'reji'))  # concatenation 
print(test([1,2,3],[3,2,4]))  # concatenation 


# so one operator which behaves differently 



# another example of polymorphism 
class ineuron:
	def msg(self):
		print('this is a msg to ineuron') 

class xyz:

	def msg(self):
		print('this is a msg to xyz') 


def test(notes):
	notes.msg() 

i = ineuron()
x = xyz()

test(i) 






