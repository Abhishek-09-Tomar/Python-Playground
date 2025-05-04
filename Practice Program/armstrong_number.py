# Topic - To check a number is Armstrong or not.

'''What is Armstrong Number ?
Answer - An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits in the number.
For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 153
'''

# take input from user
number = int(input("Enter a number to check it is an armstrong or not : "))

# logic

sum = 0

# store the number in the temp variable
temp = number

# using while loop check the condition repeatedly
while temp > 0:
    digits = temp % 10
    cube = digits**3
    sum = sum + cube
    temp //= 10

# check the condition to print the result
if sum == number:
    print(number,"is an Armstrong Number")
else:
    print(number,"is not an Armstrong Number")
