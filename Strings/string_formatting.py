# Topic - format the string with the help of using the "f" string.

name = input("Enter your name : ")
address = input("Enter your address : ")

template = "Hello, I am {} from {}."
print(template.format(name,address))

# Do this with the help of f string.
print(f"My name is {name} and i am from {address}")

