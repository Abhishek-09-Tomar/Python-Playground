# Topic - Dictionaries in python

"""
A dictionary in Python is a built-in data structure that stores data in key-value pairs. It is unordered, mutable, and indexed by keys. Dictionaries are created using curly braces {}, with key-value pairs separated by commas and a colon separating the key and value.
"""

# creating a dictionaries
country_capitals = {"Germany": "Berlin", "Canada": "Ottawa", "England": "London"}
print(country_capitals)

# print the key of the dictionary
print(country_capitals.keys())

# print the values of the dictionary
print(country_capitals.values())

# remove all the key and values from the dictionary
country_capitals.clear()
print(country_capitals)

# print table of 5 in the dictionary
table_of_5 = {i : 5*i for i in range(1,11)}
print(table_of_5)