# Topic - find the sum of n natural numbers

number = int(input("enter the number : "))

# calculate with the help of using the while loop

sum = 0

if number < 0:
    print("Please enter a positive number")
else:
    sum = 0
    while number > 0:
        sum += number
        number -= 1
    print(sum)