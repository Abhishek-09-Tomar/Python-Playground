# Topic - Function in Python

a = 12
b = 43
c =85

average = (a+b+c)/3
print("The average of these three numbers is ", average)

# Function in python is defined with def keyword.
def average(j,k,l):
    avg = (j+k+l)/3.0
    return avg

average(3,4,5) # calling function

# store the value of average in result variable
result = average(4,3,2)
print(result)

# add function
def add(c,d):
    res = c + d
    return res

output = add(d = 8, c = 9)
print(output)

# greeting function
def greet():
    """This is a docstring and that function return the greeting"""
    return "Hello!"

# greet()

val = greet()
print(val)