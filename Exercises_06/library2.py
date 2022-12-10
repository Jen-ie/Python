# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:11:15 2022

@author: Jen
"""

from math import sqrt 
print("Input lengths of the two short triangle sides:") 
a = float(input("a: ")) 
b = float(input("b: ")) 
c = sqrt(a**2 + b**2) 
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))