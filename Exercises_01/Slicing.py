#Slicing
#uses square brackets, first is starting position (0 = start, -1 = from end) second is end position and last is increment
a = "Greetings!"
#slicing starting with first character up to but not including character 4, increments of 1
print (a[0:4:1])
#slicing from final charachter, to -5 in increments of 1
print (a[-1:-5:-1])
#slicing to show only charachter 5
print (a[5])
b = "Jennifer"
#first 2 letters
first_letters = b[0:2:1]
last_letter = b[-1]
insert_letter = "a"
c = first_letters + insert_letter + last_letter
print (c)

first_character = "l"
second_character = "4"
a = first_character + second_character
print(a)
first_number = 1
second_number = 2
a = first_number + second_number
print (a)
#creating a string and demonstrating the upper and lower functions
my_string = "Almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")