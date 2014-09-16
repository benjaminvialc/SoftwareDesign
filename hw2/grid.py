# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 22:21:14 2014

@author: benjamin
"""

def dos(f):
    f()
    f()
    
def cuatro(f):
    dos(f)
    dos(f)

def vertical():
    print '!    ',
    
def horizontal():
    print '+----',
    
def verticales():
    dos(vertical)
    print '!'

def horizontales():
    dos(horizontal)
    print '+'
    
def fila():
    horizontales()
    cuatro(verticales)
    
def grid():
    dos(fila)
    horizontales()
    
grid()


        