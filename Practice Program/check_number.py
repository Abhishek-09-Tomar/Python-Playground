# Topic - check the number that it is positive, negative or zero.

# Take the input from the user
number = int(input("Enter a number : "))

# check the condition
if(number == 0):
    print("Number is 0, neither positive or negative number")

elif(number > 0):
    print(number,"is a positive number")

else:
    print(number,"is a negative number")