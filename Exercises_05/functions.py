# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:10:30 2022

@author: Jen
"""

def name_of_function():
    """
    Simple test function 
    """
    print("Yoo hoo!")

name_of_function()

#################

def name_of_function(first_name):
    """ 
    Simple test function 
    """ 
    print(f"Yoo hoo, hello {first_name}!") 
    
name_of_function("Jen")

def calculate_circumference(radius): 
    """ 
    Calculate the circumference of a circle based on its radius 
    """ 
    return 2 * 3.142 * radius 
a = calculate_circumference(5) 
print("")
print("A function is defined to calculate the circumference of a circle based on a radius of 5\nand the answer is as follows: ")
print(a)

def calculate_circumference(radius = 1): 
    """ 
    Calculate the circumference of a circle based on its radius 
    """ 
    return 2 * 3.142 * radius 
a = calculate_circumference() 
print("")
print("A function is defined to calculate the circumference of a circle based on a radius of 1\nand the answer is as follows: ")
print(a)

def calculate_circumference(radius): 
    """ 
    Calculate the circumference of a circle based on its radius 
    """ 
    return 2 * 3.142 * radius 
    # Get a radius value as a string r = input("Provide a radius value: ") 
    # Convert it to a float r_float = float(r) 
    # Call the function and create the variable for the return value 
    a = calculate_circumference(r_float) 
    print(a)
    
    
def auto_adder(*my_numbers): 
    final_number = 0 
    for number in my_numbers: 
        final_number = final_number + number 
    return final_number 
print(" ")
print("A function is defined to automatically add numbers in a list: ")
print(auto_adder(12,34,23,66,8, 99))

def most_expensive(price_list): 
    """ 
    Iterate through a list and find the most expensive item 
    """ 
    # Set up the variables 
    max_price = 0 
    max_price_item = "" 
    # Iterate, unpacking the tuple 
    for description, price in price_list: 
        # If this is the maximum price, record that in our variables 
        if price > max_price: 
            max_price = price 
            max_price_item = description 
        # If it is not the maximum price, do nothing 
        else: pass 
    # Return the maximum prices item and its price 
    return max_price_item, max_price 
# Provide the data 
price_list = [("Pineapple", 1.0), ("Apples", .5), ("Pears", .7), ("Peaches", .8)] 
# Call the function and unpack its return values 
product, price = most_expensive(price_list) 
print(" ")
print("A function was defined to find the most expensive item in a list, and \
      its cost.\nIn this case, the answer is:")
print(product, price)

"""
Changing the penultimate line to
product, price, availability = most_expensive(price_list)
gives the following output:
   ValueError: not enough values to unpack (expected 3, got 2)
This is because the pricelist containes tuples which only have 2 values, so the
programme can't find a third.

"""
print(" ")
def double_number(n: int)->int: 
    """ 
    Simple function to double a number 
    """ 
    return n+n 

# Create a list of numbers for testing 
my_numbers = [1,2,3,4,5] 
# Map my_numbers to the double_number function, return type is map 
result = map(double_number, my_numbers) 
# Print a list of the map 
print(list(result)) 
# Or iterate through it 
for item in map(double_number, my_numbers): 
    print(item)
    
print(" ")
circumference = lambda radius : 2 * 3.142 * radius 
area = lambda radius : 3.142 * radius * radius 
radius = 5 
print(circumference(radius), area(radius))

print(" ")
my_string = "global" 

def my_function(): 
    my_string = "enclosing" 
    def nested_function(): 
        my_string = "local" 
        print(my_string) 
    nested_function() 
    return my_string 
    
# Print the variable my_string 
print(my_string) 
# Print the output of the function, my_function 
print(my_function())

my_string = "global" 
def my_function(): 
    global my_string 
    print(f"At the moment, my_string is: {my_string}") 
    my_string = "mangled!" 
my_function() 
print(f"Now the global value of my_string is: {my_string}")

