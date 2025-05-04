# Topic : Program to print all prime numbers in an Interval

# prime number - having only 2 factors

# take input from the user
lower_limit = int(input("Enter the lower limit of a number : "))
upper_limit = int(input("Enter the upper limit of a number :"))

# logic to print all the prime number in an interval

for num in range(lower_limit, upper_limit + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
            else:
                print(num)
                break