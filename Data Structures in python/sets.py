# Topic : sets in python

"""Sets : a set is an unordered collection of unique elements.

Sets are denoted within the curly braces{} like :

mySet = {1,2,3,4,5,6,7,8,9}

sets are mutable that means you can add or remove the elements in a set.

"""

sets = {1,2,3}
print(sets)
# output : {1,2,3}

"""You can also create a set from a list using the set() constructor:"""

# list of elements
my_list = [34,65,345,567,3,576,6,35,86,46,867]

my_set = set(my_list) # here we create a set from the list by using a function name set which is well defined in the python programming.
print(my_set) # print the output of the set.

# now we use some set methods to manipulate the set and play with the set more.

# Creating two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# discard an element from the set
# this function is used to remove the element from the set if they are present and if they are not present python didn't through an error
set1.discard(43) 

# Add a new element
set1.add(6)

# Update set with multiple elements
set1.update([7, 8])

# Remove an element
set1.remove(2)

# Union of two sets
union_set = set1.union(set2)

# Intersection of two sets
intersection_set = set1.intersection(set2)

# Difference of two sets
difference_set = set1.difference(set2)

print("Set1:", set1)
print("Set2:", set2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
