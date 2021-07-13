#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:33:30 2021

@author: thomas
"""

import mod1 
import logging as lg 


lg.basicConfig(filename = 'even.log', level = lg.INFO,
               format='%(asctime)s %(message)s') 


while True:
    try:
        a = int(input('enter the input: '))
    except  Exception as e:
        lg.error(e) 
    else:
        print(mod1.get_even(a))
        break
    finally:
        print('closing')
    
