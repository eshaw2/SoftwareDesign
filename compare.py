# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:47:52 2014

This program compares 2 inputted values. When both values
are the same, it returns 0. When the first value is greater,
it returns 1. When the second is greater, it returns -1.

@author: elena
"""

def compare():
    x= int(raw_input('x value?'))
    y= int(raw_input('y value?'))
    
    if x>y:
        print '1'
    elif x == y:
        print '0'
    elif x<y:
        print '-1'
        
compare()
