# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:01:10 2022

@author: Jen

This code demonstrates iteration using a 'for loop'
"""

iterable_variable = [1,2,3,4,5,6] 


for item in iterable_variable: 
    # For each item, execute this code block 
    print(item)
    
#This code prints odd numbers
print("The odd numbers are as follows: ")
for item in iterable_variable: 
    if item %2 != 0:
        print(item)

#This code prints even numbers
print("The even numbers are as follows: ")          
for item in iterable_variable:        
    if item %2 == 0:             
        print(item)
        
        
print("If we add each number in the list we get: ")
total = 0 
for item in iterable_variable: 
    total = total + item 
    print(total)

print(" ")
print("To iterate over the letters in a name and search for a match - we're looking for an 'e'")  
# Define a string to iterate over 
for this_letter in "Jennifer Burns": 
    # Specify which letter to test for 
    if this_letter == "e": 
        # Found the test letter 
        print(f"Woo hoo, found a {this_letter}!") 
        # Exit the current loop 
        break 
    else: 
        # Didn't find the test letter 
        print(f"Aww man, I didn't want a {this_letter}!")

print(" ")
print("To find a number in a list - my number is 3: ")
my_number = 3
my_list = [1,2,3,0] 
for my_number in my_list: 
    if my_number == 1: 
        pass 
    if my_number == 2: 
        continue 
    if my_number == 3: 
        print(f"Found the number {my_number}") 
    if my_number == 0: 
        break
    
#printing items in list of tuples
print(" ")
print("Iterating over a list of tuples: ")
list_of_tuples = [(1,2), (3,4), ("A", "B")] 
for item in list_of_tuples: 
    print(item)


# Tuple unpacking 
print(" ")
print("Unpacking tuples: ")
list_of_tuples = [(1,2), (3,4), ("A", "B")] 
for a,b in list_of_tuples: 
    print(a) 
    print(b)

print("printing items in a range from 1 - 100, in increments of 5:") 
for index in range(1, 100, 5): 
    print(index)
    
    
#Dictionary
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"} 
for ipv4, port in scan.items(): 
    print(f"Found a service on {ipv4} at {port}")
    