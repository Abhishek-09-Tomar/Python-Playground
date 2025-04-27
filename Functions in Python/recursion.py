# Topic - Recursion

"""Recursion : calling itself repeatedly

fibonacci series : 0 1 1 2 3 5 8 13

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(n) = fib(n-2) + fib(n-1)

"""

def fibonacci(n):
    # base case of recursion
    if(n==0 or n==1):
        return n

    return fibonacci(n-2) + fibonacci(n-1)

result = fibonacci(6)
print(result)


# code
def fibo_series(n):
    a,b = 0,1
    for _ in range(n):
        print(a,end=' ')
        a,b = b,a+b

fibo_series(5)
