



class Tyres:
	def __init__(self,branch, belted_bias, opt_pressure):
		self.branch = branch
		self.belted_bias = belted_bias 
		self.opt_pressure = opt_pressure

	def __str__(self):
		return "Tyres: \n \tBranch :" + self.branch+"\n \tBelted-bias: " + str(self.belted_bias)+"\n \tOptimal pressure : " + str(self.opt_pressure)

# ob = Tyres('adiidas', 2.3, 'sdf291')
# print(ob)
	
class Engine:
	def __init__(self,fuel_type, noise_level):
		self.fuel_type = fuel_type 
		self.noise_level = noise_level

	def __str__(self):
		return	"Engine: \n \tFuel type :"+self.fuel_type + "\n \tNoise level :" +str(self.noise_level)

class Body:
	def __init__(self, size):
		self.size = size 
	def __str__(self):
		return "Body: \n \tSize :"+ str(self.size) 

class Car:
	def __init__(self,name,tyres, engine, body):
		self.name = name 
		self.tyres = tyres
		self.engine = engine
		self.body = body
	def __str__(self):
		return str(self.tyres)+"\n"+str(self.engine)+"\n"+str(self.body)+"\n"+str(self.name) 

# Notes 
# In encapsulation, we wont make all variables avilable to the some other class 
# we are trying to call the attributes by using the 
# the respective objects 
# 
t = Tyres('Pirelli', True, 2.0) 
e = Engine('Diesel', 3) 
b = Body('Medium') 
c = Car('toyoto', t, e , b) 


# print(c)



class Parent:
	attr1 = 10 
	attr2 = 40 

	def __init__(self, parent_a, parent_b):
		self.parent_a  = parent_a 
		self.parent_b = parent_b 

class child(Parent):
	def __init__(self, *args):
		super(child, self).__init__(*args) # inheritance 



# Notes 
# In inheritance, all the variables and methods are availbale to the child classs 


############ 
# other examples

class Dog:
	def __init__(self, name, year_of_birth, breed):
		self.name = name 
		self.year_of_birth = year_of_birth 
		self.breed = breed

	def __str__(self):
		return "Dog : \n  \tName: "+str(self.name)+ "\n\tYear_of_birth: "+ str(self.year_of_birth)+ "\n\tBreed = "+ str(self.breed) 


kudrja  =Dog('kudrja', 2014, 'Laika') 
# print(kudrja)



class Student:
	def __init__(self, name , student_id, school_name):
		self.name = name 
		self.student_id = student_id 
		self.school_name = school_name

	def __str__(self):
		return str(self.name)+" / " + str(self.student_id)  + " / " + str(self.school_name)

st = Student('thomas', 11 ,'st.thomas') 
# print(st) 
dg_st = Student(kudrja, 12, 'stf') 
# print(dg_st) 




# class object 
# polymorphism 
# encapsulations 
# inheritances 
# abstraction 


########################## EXAMPLE #######################33 




