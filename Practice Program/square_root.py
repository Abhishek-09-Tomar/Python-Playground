# Topic - to find the square root of a number

# method - 1 : using the Exponentiation

# take the input from the user
num = float(input("Enter the number :"))

square_root = num ** (1/2)

print("The square root of ", num, "is : ", square_root)


# method - 2 : by using the math module we find the square root of the number.

# import the math module to use the sqrt() function to calculate the square root of the number.
import math

# take input from the user
number = float(input("Enter a number to find the square root : "))

# using the sqrt() function from math module
squareRoot = math.sqrt(number)

# print the result
print("The square root of the number : ", squareRoot)

