# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:35:22 2022

@author: Jen
"""

x = 0 
while x < 10: 
    print(f"X is = {x}") 
    x = x + 1 
else: 
    print(f"As x is now = {x}, we are all finished")


#to create a list with each letter in a string
print(" ")
print("Creating a list of letters from the string 'Morning Folks!'")
my_list = [] 
my_string = "Morning Folks!" 
for letter in my_string: 
    my_list.append(letter) 
print(my_list)


print(" ")
print("Creating a list of numbers from a range 0 - 19:")
my_list = [number for number in range(0,20)] 
print(my_list)


print(" ")
print("Creating a list of numbers from the same range, each number multiplied by 10:")
my_list = [number * 10 for number in range(0,20)] 
print(my_list)


print(" ")
print("Creating a list of numbers from the range and multiplying by 10, if the number is less than 10: ")
my_list = [number * 10 for number in range(0,20) if number < 10] 
print(my_list)

