#String Interpolation
#concatenate with + to give text and a variable
a = "would you like brekkie?"
print("Good morning, Jen " + a)
#
a = 5
b = 12
print("Good mornign, Jen. For breakfast, would you like {}?".format("Fruit"))
print("We have {} apples, {} bananas and a total of {} pieces available.".format(a, b, a+b))
a = "Good"
b = "Jen"
c = "morning"
print("Messsage is: {first} {third} {second}".format(first=a, second=c, third=b))
Number = 12345
Divisor = 333
Result = Number/Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))
print(f"Result of {Number} divided by {Divisor} is {Result}")
#suppressing the automatic /n at the end of a printed line
print("Good morning, Jen", end=" ")
print("Brekkie?")
#using /n to do multi-line print (\t would enter tab character)
print("Good morning, Jen\nWould you like brekkie?")
#Getting the length of a string
a = "Good morning, Jen\nWould you like brekkie?"
print(len(a))