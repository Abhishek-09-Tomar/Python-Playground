# Topic - print fibonacci sequence

''' Fibonacci Sequence - Program to Print Fibonacci Series | GeeksforGeeksThe Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers, starting with 0 and 1. The series is typically represented as: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
'''

# method 1 to find the fibonacci series using the iterative method.

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# print the fibonacci series upto 10
fibonacci_iterative(10)

# --------------------------------------------------------------------------------------------------------------------

# method 2 to find the fibonacci series using the iterative method.

m = 0
n = 1

num = int(input("\nEnter a number : "))
if num == 1:
    print(m)

else:
    print(m)
    print(n)

    for i in range(1,num+1):
        next_term = m + n
        m = n
        n = next_term
        print(next_term)


# ----------------------------------------------------------------------------------------------------------------

# method 3 to find the fibonacci series using the Recursive method.

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(10):
    print(fibonacci_recursive(i), end=" ")