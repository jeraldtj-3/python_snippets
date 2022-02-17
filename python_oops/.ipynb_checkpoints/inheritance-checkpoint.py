
# creating the parent class 
class test:
    def __init__(self,a,b,c,d):
        self.__a = a 
        self.b = b 
        self.c = c 
        self.d = d 
    def test_custom(self,v):
        return v - self.__a 
    
    def __str__(self):
        return 'this is my test code for abstraction' 
    

class test1(test):
    def __init__(self,j, *args):
        super(test1,self).__init__(*args)
        self.j = j 

obj2 = test1(5,4,6,7,49) 
obj2.j

# able to access the methods in parent class 
obj2.test_custom(200) 


########## assignment 

class test1:
    def __init__(self):
        pass

    def func(self):
        print('this is func of test1 class') 
    
 
class test2:
    def __init__(self):
        pass

    def func(self):
        print('this is func of test2 class')    
    
    
# possible?  
class bee(test1,test2):
    # the following foo will print both func from test1 and test2 
    def foo(self):
        super (bee,self).func() 
        
        
obj = bee(); 
obj.foo();
        
        
        
############################################### 
# simple inheritance example 
class Ineuron:
    company_website = 'https://ineuron.ai'
    name = 'Ineuron' 
    
    def contact_details(self):
        print('contact us at', self.company_website)
        
class Datascience(Ineuron):
    def __init__(self):
        self.year_of_establishment = 2018 
    def est_details(self):
        print("{0} company was established in {1}".format(self.name, self.year_of_establishment))
  
ds = Datascience() 
ds.est_details()  

###############################################
# multi inheritance 
# giving priority to classes while doing multi inheritance 
class OS:
    multi_tast = True 
    os_name = 'Windows os' 
    name = 'thomas'

class windows(OS, Ineuron):
    def __init__(self):
        if self.multi_tast is True:
            print('multi task')
            print('name',self.name)  #  change the name 

windows = windows()


########################################
# multilabel inheritance
class Ineuron:
    num_of_courses = 12 

class Datascience(Ineuron):
    course_type = 'data science'

class AI(Datascience):
    def __init__(self):
        self.company = 'ineuron'
        print('the company {0} offers {1} differnt types of courses'.format(
            self.company,self.num_of_courses))
        
   
AI = AI()         
   

############################################## 
    
   
    
   

   
    
   
    
        
        
        
        
        