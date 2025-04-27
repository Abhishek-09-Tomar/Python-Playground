# list methods in python

lst = [34,54,65,34,65]

lst.append("Hindi") # This will add the new elements in the list.
print(lst)

print(lst.pop()) # This will pop up(or remove) the last element from the list.

lst.insert(0,"Tom") # insert the elements at a specific indices such as(0,1,2,3,4,5,etc.)

# copy the elements of the list.
print(lst.copy())

# extend() - add the element in list at the end of the list.

lst.extend("Hello") # they add the unique elements here they add hello like 'h', 'e', 'l', 'l', 'o' and it is 5 elements in the list.
print(lst)
print(lst.__len__()) # it will print the total elements present in the list.

lst.reverse() # it will reverse the list of element(or list).

lst.remove("H") # this removes the element 'h' from the list.

print(lst)
