# Topic - find the largest number among three numbers

# three numbers are given to check which one is greater
# a,b,c = 23,34,45

# you can also use take input from the user to check which number is greater among these three numbers.
a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
c = int(input("Enter your third number :"))

# check the condition of numbers which one is greater
if(a > b and a > c):
    print(a," is greater than b and c")

elif(b > c and b > a):
    print(b," is greater than a and c")

elif(a == b == c):
    print("All three numbers are equal")

else:
    print(c," is greater than a and b")

