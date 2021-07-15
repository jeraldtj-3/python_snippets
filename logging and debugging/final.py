

import logging 
import employee

'''
logging levels 

DEBUG - Detailed information, typically of interest only when diagisingproblems 
INFO - Confirmation that things are working as expected. 
WARNING - An indication that something unexpected happend, or indicative
        of some problem in the near future.
ERROR - Due to more serious problem, the software has not been able to perorm some function 
CRITICAL - A serious error, indicating that the program itself may be unable to continue running. 
'''

# adding the name for the logger 
logger = logging.getLogger(__name__)

# setting the logging level 
logger.setLevel(logging.DEBUG)

# Setting the logging format 
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s::%(message)s')

# adding the file name 
file_handler = logging.FileHandler('final.log')

# adding formatter to the log file 
file_handler.setFormatter(formatter) 

file_handler.setLevel(logging.ERROR) 


# adding streamhandler 
stream_handler = logging.StreamHandler() 
stream_handler.setFormatter(formatter)



# connecting the filehandler to the logger 
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


"""
# logging basic configuration ( setting the logfile and the level)
logging.basicConfig(filename = 'final.log',level = logging.DEBUG,
    format = '%(asctime)s:%(levelname)s:%(name)s::%(message)s')
"""


def add(x,y):
    """ adding function"""
    return x+y 

def substract (x, y):
    """ substracting function """
    return x-y 

def divide(x,y):
    """dividing function """ 

    try:
        result = x/y
    except ZeroDivisionError:
        # logger.error('tried to divide by zero')
        logger.exception('Tried to divide by zero')
    else:
        return result 


num_1 = 32
num_2 = 0


add_result = add(num_1, num_2) 
substract_result = substract(num_1, num_2) 
divide_result = divide(num_1, num_2) 


# first lets try with print statement 

# print("add_result",add_result)
# print("substract_result",substract_result)
# print("divide_result",divide_result)

# trying with warnings 

#logging.warning(f'add_result = {add_result}')
#logging.warning(f'substract_result ={substract_result}')
#logging.warning(f'divide_result ={divide_result}')


# with debug after the configuration 
logger.debug(f'add_result = {add_result}')
logger.debug(f'substract_result ={substract_result}')
logger.debug(f'divide_result ={divide_result}')

# source = logrecord attributes. 


