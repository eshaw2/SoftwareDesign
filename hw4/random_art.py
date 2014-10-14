# -*- coding: utf-8 -*-
"""
Random_art.py

This program generates computational image pieces using randomly 
generated functions that evaluates every pixel in the image for
its red, green, and blue values.

@author: Elena Shaw, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image, math, decimal


def build(a,b):
    """ This function builds a composite function using nested lists.
    The depth of nesting is a randomly picked number between integers a and b.
    """
    n = randint(a,b)
    funclist= {1:'prod', 2:'cos_pi', 3:'sin_pi', 4:'tanh', 5:'square'}
    varilist= {1:'x', 2:'y'}    
    genfunc = []    
    if n == 0:
        genfunc = [varilist[randint(1,2)] ]       
        return genfunc
    else:
        n=n-1    
        pickfunc= randint(1,5)
        if pickfunc == 1:
            genfunc= [funclist[pickfunc],build(n,n),build(n,n)]
        else:   
            genfunc= [funclist[pickfunc],build(n,n)]        
        return genfunc 
    return genfunc

def evaluate(f, a, b):  
    """ Evaluate the function by identifying the named string operator and
    calculate a float output using an x input of integer a and y 
    input of  integer b.
    """    
    if len(f) == 1:
        if f[0] == 'x':
            return a
        elif f[0] == 'y':
            return b
    else:        
        operation = f[0]
        if operation == 'cos_pi':
            return math.cos(evaluate(f[1],a,b)*math.pi)
        if operation == 'sin_pi':
            return math.sin(evaluate(f[1],a,b)*math.pi)
        if operation == 'tanh':
            return math.tanh(evaluate(f[1],a,b))
        if operation == 'square':
            return math.pow(evaluate(f[1],a,b),2)
        if operation == 'prod':
            return evaluate(f[1],a,b)*evaluate(f[2],a,b)
   

def remap(val, instart, inend, outstart, outend):
    """ Maps the input value that is in the interval [instart, inend]
        to the output interval [outstart, outend].  The mapping
        is an affine one (i.e. output = input*c + b).
        All inputs can be float, but integer values are recommended
        for the input and output intervals
    """   
    delout = outend - outstart
    delin = inend - instart
    delratio = float(delout) / delin
    point = (delratio*(val - instart)) + outstart
    return point

#create an RGB image of 350 by 350 pixels
im = Image.new("RGB",(350,350))
pix = im.load()

#creat three separate composite functions to be used as red, green, and blue
rf = build(3,17)
gf = build(8,13)
bf = build(5,8)

#for every pixel in the image, evaluate the RGB value according to the 
#previously built function, then build and save the image
for i in range (0, 349):
        for j in range (0,349):
            xval = remap(i, 0, 349, -1, 1)
            yval = remap(j, 0, 349, -1, 1)
                        
            red = int(remap(evaluate(rf, xval, yval), -1, 1, 0, 255))
            green = int(remap(evaluate(gf, xval, yval), -1, 1, 0, 255)) 
            blue = int(remap(evaluate(bf, xval, yval), -1, 1, 0, 255))
            pix[i,j] = (red, green, blue)
    
im.show()
im.save('comptimg4.png')



#your additional code and functions go here
