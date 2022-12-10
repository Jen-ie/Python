# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:15:11 2022

@author: Jen
"""


cube_text = "Yo, time to cube stuff!"

def cube(x): 
    return x*x*x 


if (__name__ == '__main__'): 
    print(f"This module is called {__name__} and executes as a standalone script") 
else: 
    print(f"This module is called {__name__} and is being called by another script")


