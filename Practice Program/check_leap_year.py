# Topic : check a year is leap year or not

# leap year - 366 days
# simple year - 365 days

# take year number from the user.
year = int(input("Enter the year number : "))

# check the condition
if(year % 400 == 0 and year % 100 == 0):
    print(year,"is a leap year")

elif(year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")

# sample input : 2024
# sample output : 2024 is a leap year