# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:21:23 2022
Simple Class, by convention, use camel case to name classes
@author: Jen
"""
# Create a class 
class JensClass():
    # Constructor, called whenever an instance of the class is created. 
    def __init__(self, my_greeting): 
        print("Running constructor for JensClass") 
        # Create attributes and set initial values 
        self.message = my_greeting 
        
    def my_method(self): 
        print(self.message) 
        
my_class1 = JensClass("Morning Jen!") 
my_class1.my_method() 
print(type(my_class1))

my_class2 = JensClass("Goodnight Jen!")
my_class2.my_method()
print(type(my_class2))
