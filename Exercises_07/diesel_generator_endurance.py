# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:54:26 2022

@author: Jen
"""

fuel = 0
fuel_consumption = 0

def endurance(fuel, fuel_consumption) ->float:

    while True:
        print("If you wish to calculate diesel generator endurance ")
        #check if the value entered is a float
        try: 
            fuel = float(input("Please enter the fuel total:  "))
            fuel_consumption = float(input("Please enter the fuel consumption:  "))
        #if it's not a float a value error will be raised, ask for a number
        except ValueError:
            print("PLease enter a number!")
        #If the input is good, calculate the endurance
        else:
            
            try:
                ans = fuel / fuel_consumption
                print(f"The total for endurance is {ans}")
                break
                
            #Input of zero for fuel_consumption will result in ZeroDivisionError
            except ZeroDivisionError:
                print("You must enter a total greater than 0 for fuel consumption ")
                pass
    
            
endurance(fuel, fuel_consumption)


