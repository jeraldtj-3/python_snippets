
# single underscore : protected 
class test:
    def __init__(self,a,b,c,d):
        self._a = a 
        self.b = b 
        self.c = c 
        self.d = d 
    def test_custom(self,v):
        return v - self._a 
    
    def __str__(self):
        return 'this is my test code for abstraction' 
    

object = test(2,3,4,5)
object.test_custom(42) 
object._a

# no underscore = public 
# giving double underscore : private 
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
    

object = test(2,3,4,5)
object.test_custom(42) 

# not able to access variables outside of the class 
object.__a

# accessing using class name 
object._test__a
