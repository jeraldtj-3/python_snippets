import logging 
from logging.handlers import TimedRotatingFileHandler
import os 
import time
from pathlib import Path


logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO) 


# creating a folder for keeping the rotating log files 
my_folder = Path('./time_rotate_logs')
if my_folder.is_dir():
	pass
else :
	os.mkdir('time_rotate_logs')


# s, m , h , d , midnight, w0 for monday etc.
handler = TimedRotatingFileHandler('time_rotate_logs/time_log.log',
	when = 's', interval = 5, backupCount = 5)

for _ in range(6):
	logger.info('this info log from time_rotate_logs.py program') 
	time.sleep(5) 

