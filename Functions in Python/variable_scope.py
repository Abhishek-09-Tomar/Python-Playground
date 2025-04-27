# Topic - Variable scope in python
# Types of scope : 1. global scope and 2. local scope

"""
1. global scope : when a variable declared outside a function and can be used throughout the program.
2. local scope : when a variable is declared inside a function and can be used only inside the function only.
"""


# global scope
global a 
a = 43
print("Global scope variable: ",a)

def local_scope():
    local = 4 # local scope
    global m # here we use global keyword to make it globally accessible in the entire program.
    m = 43
    return local

print("This is a local scope variable: ", local_scope())

print(m) # globally accessible


# function with docstring.
def area_of_rectangle(length, breadth):
    """calculate the length of the rectangle."""
    area = length * breadth
    return area

rect_area = area_of_rectangle(3,4)
print("Area of rectangle : ", rect_area)


# print the docstring.
print(area_of_rectangle.__doc__)