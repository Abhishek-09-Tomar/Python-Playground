# Topic - print the multiplication table as user want.

# we solve that with two methods : 1.Using the for loop and 2.Using the while loop


# Method - 1 : Using the for loop
# Enter a number you want to print the table
number = int(input("Enter a number : "))

# Logic to print the table
for i in range(1,11):
    table = i * number
    print(number,"x",i,"=",table)

# Using the while loop
num = int(input("Enter a number : "))

# while loop logic to print the table

i = 1
while i <= 10:
    print(num,"x",i,"=",num * i)
    i = i + 1

