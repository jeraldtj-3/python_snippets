#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:55:42 2021

@author: thomas
"""
import logging 
import os 
def get_logs(msg):
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
    logger.info(msg)

get_logs()


