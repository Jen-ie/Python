# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:34:58 2022

@author: Jen

This programme calculates the volume of a cylinder
"""


#The formula to calculate the volume of a cylinder is pi x radius x radius x height
print("To find out the volume of a cylinder - > ")


pi = 3.141592653589793238

def volume_of_cylinder(radius, height)->float:
    return (pi*radius*radius*height)
    

r = float(input("Please enter the radius of the cylinder: "))
h = float(input("Please enter the height of the cylinder: "))
print("The volume of your cylinder is...")

#rounding the answer to 2 decimal places
answer = round(volume_of_cylinder(r, h), 2)
print(answer)
