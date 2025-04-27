# Topic : Match case in python

a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("you won a charger")
    case 2:
        print("you won phone")
    case 3:
        print("you won a camera")
    case _:
        print("Better luck next time")