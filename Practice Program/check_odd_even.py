# Topic - check odd and even numbers.


# method - 1 :

# take input from the user to check a number is even or odd.
num = int(input("Enter a number :"))

# check the conditions
if(num % 2 == 0):
    print(num,"is even number.")
elif(num%2 != 0):
    print(num,"is odd number.")
else:
    print("Enter a valid integer number.")

# method - 2 : 

# take the input from the user.
number = int(input("Enter a numeber : "))

if(number % 2 == 0):
    print(number,"is an even number")
else:
    print(number,"is a odd number")