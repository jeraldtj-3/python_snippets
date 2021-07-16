

class test:
	def __init__(self, a ,b, c):
		self.a = a 
		self.b = b 
		self.c = c 
	def __str__(self):
		return 'this is the return from my test class'

class test1:
	def __init__(self, a ,b, c):
		self.a = a 
		self.b = b 
		self.c = c 
	def __str__(self):
		return 'this is the return from my test1 class'

class test2:
	def __init__(self, a ,b, c):
		self.a = a 
		self.b = b 
		self.c = c 
	def __str__(self):
		return "this is the return from my test2 class" 

class final:
	def __init__(self, test, test1, test2):
		self.test = test
		self.test1 = test1 
		self.test2 = test2 
	def __str__(self):
		return  str(self.test) + " --" + str(self.test1) + " --" + str(self.test2)  

t = test(4,5,6)
t1 = test1(3,4,5)
t2 = test2(5,6,7) 
# passing all these class objects
f = final(t, t1,t2) 

print(f)

f1 = final(t, t1, 'thomas') 
print(f1)

