# Topic -  find the factorial of a number.

# Here we find the factorial with two methods one is iterative method and second one is recursive method

# number less than zero factorial does not exist.

# NOTE - Factorial of 0 is 1


# Method - 1 :

# take a number you want to find the factorial of a number
number = int(input("enter a number to find factorial : "))

# logic to find the factorial
fact = 1

if number < 0:
    print("factorial does not exist !")
if number == 0 :
    print("The factorial of 0 is 1")
if number > 0:
    for i in range(1,number + 1):
        fact = fact * i

print("The factorial of",number,"is", fact)

# Method - 2 :

# logic to find the factorial using the recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return ((num) * factorial(num - 1))

# Take a number as an input from the user.
num = int(input("Enter a number to find factorial : "))

# they return the result of the factorial
result = factorial(num)

# print the result of the given number factorial
print("The factorial of",num,"is",result)
