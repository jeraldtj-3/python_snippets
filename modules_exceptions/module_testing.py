#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 21:56:53 2021
@author: thomas
"""
from test_directory import mod1, mod2, mod3
import module1
from module1 import get_course

# for reloading the module 
# import imp

# imp.reload(module1)

module1.addition(1, 4)
module1.power(3, 3)

module1.get_course()
print(module1.data)
module1.get_msg()

get_course()

# assignment 
# test directory 
# inside this module1.py  ( fn1, fn2, fn3)
# module2.py ( fn21, fn22, fn23) 
# module3.py (fn31) 
# inside same directory 
# import all
# inside test there is test1 


# calling functions
mod1.fn3()
mod2.fn23()
mod3.fn31()



