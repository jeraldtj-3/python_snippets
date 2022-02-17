

import logging

# adding the name for the logger 
logger = logging.getLogger(__name__)

# setting the logging level 
logger.setLevel(logging.INFO)

# Setting the logging format 
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# adding the file name 
file_handler = logging.FileHandler('employee.log')

# adding formatter to the log file 
file_handler.setFormatter(formatter) 


logger.addHandler(file_handler)

'''

# fundamental 
logging.basicConfig(filename = 'employee.log',level = logging.INFO,
	format = '%(levelname)s:%(name)s:%(message)s') 
'''


# Creating the employee class 
class Employee:
	''' A sample employee class''' 
	def __init__(self, first, last):
		self.first = first 
		self.last = last 

		logger.info(f'Created Employee: {self.first}-{self.email}') 

	@property
	def email(self):
		return f'{self.first}.{self.last}@gmail.com'

	@property
	def fullname(self):
		return f'{self.first} {self.last}' 


# creating some instances 
emp_1 = Employee('John', 'Smith') 
emp_2 = Employee('Thomas', 'Reji')
emp_3 = Employee('Merin', 'James')





