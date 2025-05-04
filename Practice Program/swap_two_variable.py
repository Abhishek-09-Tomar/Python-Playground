# Topic - Swap two variable

# method -1 : using the temperory variable.

# two variable are given
a = 550
b = 400

# swap these two variable - a becomes 400 and b becomes 550.
temp = a
a = b
b = temp

# print the result
print("a =",a,"b =",b)

# method - 2 : without using the third variable.

# given values
x = 3
y = 5

# swap the values
x,y = y,x

# print the swaped values
print("x=",x,"y=",y)