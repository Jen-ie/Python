# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:28:23 2022

@author: Jen
This program returns true or false based on criteria being met.
"""

def divisible(numerator: int, denominator: int)->bool: 
    return numerator % denominator == 0 

print(" ")
print("The first function returns the answer True if the first number divided by the second = 0")
print(divisible(30,30))

def find_num(number_list: list, number: int)->bool: 
    for iterate_number in number_list: 
        if iterate_number == number: 
            return True 
        else: 
            pass 
        
result = find_num([1,2,3,4,5,6,7,8], 8) 

print(" ")
print("The second function returns True if a number is found in the list")
print(result)


def find__even_num(number_list: list)->bool:
    for iterate_number in number_list: 
        if iterate_number % 2 == 0: 
            return True 
        else: 
            pass
        
result = find__even_num([1,2,3,4,5,6,7,8])
print(" ")
print("The third function returns True if there is an even number in the list")
print(result)
print(" ")