# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:14:32 2022

@author: Jen
"""

square_text = "You wanted it squared?? "
def square(x): 
    return x*x 

if (__name__ == '__main__'): 
    print(f"This module is called {__name__} and executes as a standalone script") 
else: 
    print(f"This module is called {__name__} and is being called by another script")
    


