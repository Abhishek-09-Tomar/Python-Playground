# Topic : String Method in Python

# String are immutable
name = "Harry"

# name[0] = "m" # they show you error

print(name[0])

print(name.upper()) # this will change the string in the uppercase.
print(name.lower()) # this will change the string in the lowercase.
print(name.capitalize())
print(name.title())

last_name = " sparrow"
print(last_name.strip())    # strip method is used to remove extra whitespaces.
print(last_name.lstrip())   # left strip method is used to remove extra whitespaces from the left only.
print(last_name.rstrip())   # right strip method is used to remove extra whitespaces from the right only.


# length of the string : this will find with the method name len().
print("the length of the string name is : ", len(name))
# some more string methods in python that will use more frequently

quote = "That is a quote"

find = quote.find("a")
print(find)

# this will replace
replace = quote.replace("is", "are") # here we replace "is" with "are". and the new sentence will became "This are a quote"

print(replace)

# split function in python
fruits = "Apple, Banana, Mango"
print(fruits.split(","))    # This will return a list of fruits.

print(",".join(['Apple', ' Banana', ' Mango'])) # this will return the string.