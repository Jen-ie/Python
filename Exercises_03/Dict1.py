#creating a dictionary
my_dictionary = {"FName":"Jen", "SName":"Burns", "Occupation":"Executive Officer"}
print(my_dictionary)
print("Works as a " + my_dictionary["Occupation"])
#values from dictionary are retrieved using key, not index. Keys are always strings
#adding to a dictionary
my_dictionary["salary"] ="not enough!"
print(my_dictionary)
#editing a value in a dictionary
my_dictionary["Occupation"] = "Brain Surgeon!"
print(my_dictionary)
#print just the keys
print(my_dictionary.keys())
#print just the values
print(my_dictionary.values())
#print the items
print(my_dictionary.items())