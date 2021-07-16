
# creating class Car 
class Car():
    def __init__(a, m, y, ma, mo):
        a.milage = m 
        a.year = y 
        a.make = ma 
        a.model = mo
    def age(b, current_year):
        return current_year - b.year
    def get_milage(self):
        print(f'milage = {self.milage}')
    # instructions while printing an object of a class 
    # here we are overriding the __str__() method 
    def __str__(self):
        return "this is an object in the Car class"
# creating an object     
nano = Car(20, 2012, 232214, "asfo123")

print('nano = ', nano)
print('milagee = ', nano.milage)




class Student:
    def __init__(self, name, rollno, joining_date, current_topic):
        self.name = name 
        self.rollno = rollno 
        self.joining_date = joining_date 
        self.current_topic = current_topic 
    
    def name_parsing(self):
        if type(self.name) == list:
            for i in self.name:
                print(f'name of the student = {i}') 
        else : 
            print('provided name is not in the form of list')
            
    
    def crt_topic(self):
        print(f"current topic discussed in class is {self.current_topic}")
        
    def str_rollno(self):     
        try:        
            if type(self.rollno) == str:
                print('do nothing')
            else:
                return str(self.rollno) 
        except Exception as e : 
            print('exception happend',e)  
            
            
    def duration(self, current_date):
        print(f'duration of student is {current_date - self.joining_date}')
        
    def __str__(self):
        
        return "this object belongs to student calss "



student1 = Student('Thomas', 11, 2021, 'python oops') 
pawan = Student(["navin", "jay", "himanshu"], [123,123,132], 2021, "oops") 




'''
Assignment question : 
class - data 
variables  - file name , file type , date, size 
file_open ( create that specified file name / write sth in the file ) 
file_read (file_name) -- just read 
append_new ( add new data in the file and show) 

'''
print('hi')


import os 
import logging 

class Data:
    def __init__(self, file_name , file_type, date,size):
        self.file_name = file_name 
        self.file_type = file_type
        self.date = date 
        self.size = size
        self.file = f'{self.file_name}.{self.file_type}'
        self.get_infologs('Data Added')
        
    def f_open(self):
        # creating a the specified file and entering data 
        f = open(self.file, 'wt') 
        content = input() 
        f.write(content)
        f.close()
        self.get_infologs('file created and closed')
        
    
    def f_read(self):
        # reading only 
        try:         
            f  = open(self.file, 'r') 
        except Exception as e:
            self.get_infologs('exception',e)
        finally:
            f.close()
    
    def f_append(self):
        try:
            text_for_append = input() 
            f = open(self.file, 'a') 
            f.write(text_for_append)
        except FileNotFoundError:
            self.get_infologs('file doesnt exist') 
        else:
            self.get_infologs('appended information')
        
    
    
    def get_infologs(self,inform):
        # adding the name for the logger 
        logger = logging.getLogger(__name__)
        # setting the logging level 
        logger.setLevel(logging.INFO)
        # Setting the logging format 
        formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
        # adding the file name 
        file_handler = logging.FileHandler('employee.log')
        #adding formatter to the log file 
        file_handler.setFormatter(formatter) 
        logger.addHandler(file_handler)
        logger.info(inform) 

data1 = Data('testing1', 'txt', '12/7/2021', None)
data2 = Data('testing2', 'txt','12/7/2021', None)




