# Topic - To check the armstrong number in an interval.

# take input from the user lower and upper limit
lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))

# logic

for number in range(lower_limit,upper_limit + 1):
    sum = 0
    order = len(str(number))
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if number == sum:
        print(number)