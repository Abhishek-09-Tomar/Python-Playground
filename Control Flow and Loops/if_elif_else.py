# Topic : Learn if-elif-else statement in python.

# take the age input from the user
age = int(input("Enter the age : "))

if(age>18):
    print("You can dive a car.")
elif(age > 14):
    print("You can drive a bike.")
elif(age > 5):
    print("You can drive a cycle.")
else:
    print("You cannot drive just enjoy you life ")