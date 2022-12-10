# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:44:18 2022

@author: Jen

This programme works out the remainder of my budget, taking into account various
expenses listed
"""
#The total 400 is assigned to the variable 'income'
income = 400
#The total 120 is assigned to the variable 'petrol'
petrol = 120
#The total 80 is assigned to the variable 'food'
food = 80
#The total 80 is assigned to the variable 'coffees_and_treats'
coffees_and_treats = 80
#This print statement demonstrates the income total per month
print(f"I get €{income} per month.")
#This print statement shows the money spent on each item
print(f"I spend €{petrol} on petrol, €{food} on food, and €{coffees_and_treats} on coffees and treats.")
#This print statement shows the money that's left over
print(f"This leaves me with €{income - (petrol + food + coffees_and_treats)}!")