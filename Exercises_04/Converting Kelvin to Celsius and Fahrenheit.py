# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:14:17 2022

@author: Jen

This program converts a list of temperatures in Kelvin to Celsius and Fahrenheit
"""


#print(" ")
#print("Converting depth in feet to depth in meters: ")
#conversion = 0.3048 
#my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8] 
#my_depth_in_meters = [(depth * conversion) for depth in my_depth_in_feet] 
#print(my_depth_in_meters)

print(" ")
print("Converting Kelvin to Celsius and Fahrenheit")
print(" ")
print("We have the following list of temperatures in Kelvin:")

temp_in_kelvin = [283.15, 281.15, 279.15, 278.15, 277.15, 276.15, 275.15, 274.15, 273.15, 272.15 ]
print(temp_in_kelvin)
convert_kelvin_to_celsius = -273.15
temp_in_fahrenheit = [(((temp + convert_kelvin_to_celsius) * 1.8) + 32) for temp in temp_in_kelvin]
temp_in_celsius = [(temp + convert_kelvin_to_celsius) for temp in temp_in_kelvin]
print(" ")
print("The temperatures in Celsius are as follows: ")
print(temp_in_celsius)
print(" ")
print("The temperatures in Fahrenheit are as follows: ")
print(temp_in_fahrenheit)





