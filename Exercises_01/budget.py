# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:44:18 2022

@author: Jen

This programme works out the remainder of my budget, taking into account 
expenses listed
"""

income = 400
petrol = 120
food = 80
coffees_and_treats = 80
print(f"I get €{income} per month.")
print(f"I spend €{petrol} on petrol, €{food} on food, and €{coffees_and_treats} on coffees and treats.")
print(f"This leaves me with €{income - (petrol + food + coffees_and_treats)}!")