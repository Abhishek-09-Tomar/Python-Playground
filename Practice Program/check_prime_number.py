# check a number is prime or not.

number = int(input("enter a number : "))

if(number == 1):
    print("1 is not a prime number")

for i in range(2,number):
    if(number % i == 0):
        print(number,"is not a prime number")
        break
    else:
        print(number,"is a prime number")
        break
