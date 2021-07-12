


# creating logger 
import logging as lg 
import os 
present = os.getcwd() 
os.mkdir(present+'/'+'logdir2')
os.chdir('logdir2') 
lg.basicConfig(filename='py_log.log', level= lg.INFO) 

def func1(*args):
    lg.info('you are running func1') 
    lg.info(f'user inputs are {list(args)}')
    lg.info(f'the total number of args is {len(args)}')
    output  = 0 
    for i in args:
        output+= i 
    lg.info(f'output is {output}') 
    
func1(3,2) 
func1(32,63,42,2,3,2,3) 

file= open('py_log.log','r')

file.readlines()
os.chdir(present)
lg.shutdown() 


