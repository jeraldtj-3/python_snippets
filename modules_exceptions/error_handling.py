
# compile time issues
# runtime issues 
# 
'''
we handle runtime errors
compile errors are errors due to syntax or semantics. 
runtime time errors are erros encountered at the time of code execution. 
'''

# error type 1 : compile time 
print('hello) 
      
# error type 2 
print(3/0) # runtime error 


# no file exists 
a = open('test.txt', 'r') 

# try 
try:
    a = 3/0
    a = open('test.txt', 'r')
    # print('hi')
    
except IOError:
    print('there is some issue with the code')
except ZeroDivisionError:
    print('zero division error')


try:
    a = 3/5 
    print(a)
except ArithmeticError as e:
    print('occured',e)
else:
    print('this will execute once try will execute with sucess')


'''
Whenever there is an issue in the try block it will come to 
except block. If try block executed then it will come to else block.
'''


try :
    a = int(input('enter the first number: '))
    b = int(input('enter the second number: '))
    a = a/b
    print('executing try block')
    print(a) 
    
    
except ArithmeticError as e:
    print('occurred', e) 
    f  = open('test.txt', 'w')
    f.write('this is the first line')
    f.close() 
else:
    print('executing else block')
    try : 
        f = open('test1.txt','r')
    except IOError as e:
        print('there is an issue inside else block')
 

# finally block 


l = [4,5,6,7,8,9.0] 
print(l[100]) 
t = (4,5,6,38,42) 
print(t)



try : 
    l = [3,4,24,53]
    pritn(l[100]) 
except:
    print('executing except block')
    print('there is an isuue with the try block')
    t = (3,2,4,2)
    print(t)
    try :        
        t[0] = 'thomas'
    except TypeError as  e : 
        print('error occured:', e) 
    
else:
    print('there is no issue')




try : 
    f = open('test12.txt', 'r')
except: 
    print('error occured') 
else: 
    print('executing else block') 
finally: 
    print('executing finally')
    l = [2,32,3] 
    try : 
        l[23] = 'thomas'
    except : 
        print('there is an error inside try in the finally block ')
    else : 
        print(print(l)) 

        
try : 
    f = opne('test234.txt', 'r') 
except IOError as e:
    print('this is error : ', e) 





def askforint():
    while True: 
        try: 
            a = int(input('enter an integer : '))
            output = 3/a
            
        except FileNotFoundError as e:
            print('this is my error msg', e) 
        except IOError as e:
            print('this is my error msg', e)
        except ValueError as e:
            print('this is my error msg', e)
        except Exception as e:
            print(e)
        except ArithmeticError as e :
            print('this is my error msg', e)
        except ZeroDivisionError as e :
            print('this is my error', e) 
            
        else: 
            print('output  = ', output) 
            break
        
        finally: 
            print('closing')

askforint() 


# raising exceptions 
def create_your_exception(a):
    if a == 6:
        raise Exception('six is not usable')
    else :
        return 'input is ok' 
    
    
    
try:   
    create_your_exception(6)
except Exception as e:
    print(e)


'''
assignment 
===============
create a test folder 
mod1.py - print all the even num() function 

py file - call the module  
input for the function 
try to handle all the exception 


'''





















































