my_list = ["one", "two", "three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))
#counting specific items in tuples
my_tuple = ("one", "two", "three", "one")
#how many times does "one" appear in the tuple
print(my_tuple.count("one"))
#index - find out the position of the first appearance of a specific item
print(my_tuple.index("one"))
#values can't be changed
#my_tuple[0] = "ten"
#print(my_tuple) - returns error
