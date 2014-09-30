# -*- coding: utf-8 -*-

"""
Created on Tue Sep 30 00:50:11 2014

@author: benjamin
"""

import string

def analyse(name):
    i = 0
    count = 0
    for i in range(len(sdavid)):
        if sdavid[i] == name:
            count = count + 1
    return count

     
f = open('david.txt', 'r')

david = f.read()
sdavid = string.split(david)

t = ['CHARACTERS', '','David Cooperfield', 'Agnes Wickfield', 'James Steerforth', 'Clara Peggotty', 'Little Emily', 'Uriah Heep', 'Miss Betsey Trotwood', 'Dora Spenlow', 'Mr. and Mrs. Wilkins Micawber', 'Tommy Traddles', 'Clara Copperfield', 'Mr. Edward Murdstone and Miss Jane Murdstone', 'Mrs. Steerforth and Rosa Dartle', 'Mr. Peggotty, Ham, and Mrs. Gummidge', 'Doctor Strong and Annie Strong', '']

for i in range(len(t)):
    print t[i]
    
name = raw_input('Enter name: ')
g = analyse(name)
print g
