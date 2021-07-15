import logging 
logger = logging.getLogger(__name__)
logger.info('hello from helper')

# logger.propagate = False 

# creating handler 
stream_h = logging.StreamHandler() 
file_h = logging.FileHandler('helper.log') 

# levela and the format 
stream_h.setLevel(logging.WARNING) 
file_h.setLevel(logging.ERROR) 

formatter = logging.Formatter('%(name)s : %(levelname)s : %(message)s') 
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)



logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is warning from helper.py') 
logger.error('this is an error form helper.py') 


