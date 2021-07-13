#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:30:39 2021

@author: thomas
"""

def get_even(a):
    l = [] 
    for i in range(a+1):
        if i%2 == 0:
            l.append(i)
    return l 
