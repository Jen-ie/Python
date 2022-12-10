# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:07:20 2022

@author: Jen
"""

""" 
project.py 
""" 
import reusable 
print("Running code from the project") 
print(reusable.my_square(4))

import math
print("Input lengths of the two short triangle sides:") 
a = float(input("a: ")) 
b = float(input("b: ")) 
c = math.sqrt(a**2 + b**2) 
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))



