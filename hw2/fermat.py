# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 22:51:45 2014

@author: benjamin
"""
a=int(raw_input("a="))
b=int(raw_input("b="))
c=int(raw_input("c="))
n=int(raw_input("n="))
def check_fermat():
    if n > 2 and (a^n)+(b^n)==(c^n):
         print ("Holy smokes, Fermat was Wrong")
    else:
        print ("no, that doesnt work")
check_fermat()   
    