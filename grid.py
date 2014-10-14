# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:47:52 2014

This program creates 2 sorts of grids, one 2 by 2, the
other a 4 by 4.

@author: Elena
"""
m= '- '*4
p= '+'
l= '|'
s= ' '*8


def horiz2():
    print p,m,p,m,p

def horiz4():
    print p,m,p,m,p,m,p,m,p

def vert2():
    print l,s,l,s,l
    
def vert4():
    print l,s,l,s,l,s,l,s,l
  
def v24():
    vert2()
    vert2()
    vert2()
    vert2()
  
# part 1   
def grid():
    horiz()
    v24()    
    horiz()
    v24()
    horiz()

grid()

# part 2
def v44():
    vert4()
    vert4()
    vert4()
    vert4()
    
def double_grid():    
    horiz4()
    v44()
    horiz4()
    v44()
    horiz4()
    v44()
    horiz4()
    v44()
    horiz4()
    
double_grid()