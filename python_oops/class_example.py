




class BonusDistribution:
	def __init__(self, employee_id, employee_rating):
		self.empid = employee_id 
		self.emprat = employee_rating
		self.__bonusforRatingA = "70%" # making things private 
		self.__bonusforRatingB = "60%" 
		self.__bonusforRatingC = "50%"  
		self.__bonusforRatingD = "30%" 
		self.__bonusforRatingForRest = 'No Bonus' 

	def changeVariable(self, value):
		self.__bonusforRatingB = value 


	def bonusCalculator(self):

		if self.emprat =="A":
			bonus = self.__bonusforRatingA  
			msg = "Bonus for this employee is :" + bonus 
			return msg

		elif self.emprat =="B":
			bonus = self.__bonusforRatingB 
			msg = "Bonus for this employee is :" + bonus 
			return msg

		elif self.emprat =="C":
			bonus = self.__bonusforRatingC  
			msg = "Bonus for this employee is :" + bonus 
			return msg

		elif self.emprat =="D":
			bonus = self.__bonusforRatingA  
			msg = "Bonus for this employee is :" + bonus 
			return msg

		elif self.emprat =="A":
			bonus = self.__bonusforRatingA  
			msg = "Bonus for this employee is :" + bonus 
			return msg 

		else:
			bonus = self.__bonusforRatingForRest
			msg = "Bonus for this employee is :" + bonus	
			return msg 


emp1 = BonusDistribution(11,"B")
emp2 = BonusDistribution(11,"B")
emp3 = BonusDistribution(11,"E")

print(emp1.bonusCalculator())


emp1.__bonusforRatingB = '90%' 
print(emp1.bonusCalculator()) 

# accessing the protected variable 
emp1._BonusDistribution__bonusforRatingB = "90%"
print(emp1.bonusCalculator()) 



# using a different mathod for changing 
emp1.changeVariable("85%")
print(emp1.bonusCalculator()) 


print('-----------------------------------------')
# change will happen only for specific object 
emp2.changeVariable("34%")
print(emp1.bonusCalculator()) 
print(emp2.bonusCalculator()) 

emp4 = BonusDistribution(19,"B")
print(emp4.bonusCalculator()) 
