# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:47:52 2014

Based on user input, this program verifies whether Fermat's
Last Theorem holds for the inputted values.

@author: elena
"""
# part 1
def check_fermat(a,b,c,n):
    summ = a**n+b**n
    expo= c**n
    
    if n > 2 and summ == expo:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No, that doesn't work"
        
check_fermat(1,1,1,3)


# part 2
a= int(raw_input('a?'))
b= int(raw_input('b?'))
c= int(raw_input('c?'))
n= int(raw_input('n?'))

check_fermat(a,b,c,n)