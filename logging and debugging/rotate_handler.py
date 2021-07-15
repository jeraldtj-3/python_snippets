import logging 
from logging.handlers import RotatingFileHandler
import os 
from pathlib import Path 

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO) 

# creating a folder for keeping the rotating log files 
my_folder = Path('./rotate_logs')
if my_folder.is_dir():
	pass
else :
	os.mkdir('rotate_logs')



# roll over after 2kb, and keep backup logs app.log1, app.log2, ...
handler = RotatingFileHandler('rotate_logs/app.log', maxBytes = 2000, backupCount = 10)
logger.addHandler(handler)

for _ in range(100000):

	logger.info('thi is the message from rotate hanler program') 
	logger.info('this is the second message from rotate handler program')


	