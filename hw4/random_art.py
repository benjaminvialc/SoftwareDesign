# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:33:38 2014

@author: benjamin
"""

from random import randint
import Image 
from math import *
from PIL import Image

def prod(a,b):
    return float(a)*float(b)
    
def cos_pi(a):
    return cos(pi*a)
    
def sin_pi(a):
    return sin(pi*a)

def cos_sin(a,b):
    return cos(a)*sin(b)
    
def cos2(a):
    return cos(a)*cos(a)
    
def x(a,b):
    return a

def y(a,b):
    return b
    
def creation(value):
    choosefun=randint(1,5)
    if value > 1:
        if choosefun ==1:
            return ["prod",creation(value-1),creation(value-1)]
        elif choosefun ==2:
            return ["cos_pi",creation(value-1)]
        elif choosefun ==3:
            return ["sin_pi",creation(value-1)]
        elif choosefun ==4:
            return ["cos_sin",creation(value-1),creation(value-1)]
        elif choosefun ==5:
            return ["cos2",creation(value-1)]            
        
    elif value ==1:
        choosevalue=randint(1,2)
        if choosevalue==1:
            return ["x"]
        elif choosevalue==2:
            return ["y"]
    
def build_random_function(min_depth, max_depth):
    value = randint(min_depth,max_depth);
    return creation(value);

funct = build_random_function(1,5)
print funct

def evaluate_random_function(f, x, y):
    if f[0] == 'x':
        return x
    elif f[0] == 'y':
        return y
    else:
        if f[0] == 'prod':
            return prod(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
        elif f[0] == 'cos_pi':
            return cos_pi(evaluate_random_function(f[1],x,y))
        elif f[0] == 'sin_pi':
            return sin_pi(evaluate_random_function(f[1],x,y))
        elif f[0] == 'cos_sin':
            return cos_sin(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
        elif f[0] == 'cos2':
            return cos2(evaluate_random_function(f[1],x,y))
            
            
print evaluate_random_function(funct,2,5)


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    return ((val - input_interval_start)*((output_interval_end - output_interval_start)/float((input_interval_end - input_interval_start))) + output_interval_start)
for i in range(5):
    Img = Image.new('RGB',(350,350))
    red1=build_random_function(5,5)
    blue1=build_random_function(5,5)
    green1=build_random_function(5,5)
    for x in range(0,349):
        for y in range(0,349):
            blue = remap_interval(evaluate_random_function(blue1, remap_interval(x,0, 349,-1,1),remap_interval(y,0,349, -1,1)),-1,1 , 0, 255)
            green = remap_interval(evaluate_random_function(green1, remap_interval(x,0, 349,-1,1),remap_interval(y,0,349, -1,1)),-1,1 , 0, 255)
            red = remap_interval(evaluate_random_function(red1, remap_interval(x,0, 349,-1,1),remap_interval(y,0,349, -1,1)),-1,1 , 0, 255)
                
            Img.putpixel((x,y),(int(red), int(blue), int(green)))
    
    
    Img.save('ImgExample'+str(i+1)+'.png', "PNG")


"""Maps the input value that is in the interval [input_interval_start, input_interval_end]
to the output interval [output_interval_start, output_interval_end]. The mapping
is an affine one (i.e. output = input*c + b).
TODO: please fill out the rest of this docstrin"""
  