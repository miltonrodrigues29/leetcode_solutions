# def fibonacciSum(n):


# fib1 , fib2 = 0 , 1

# fib(n) + fib(n-1)

def fibonacciSum(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibonacciSum(n-1) + fibonacciSum(n-2) + 1

print(fibonacciSum(4))

# 0, 1, 1, 2, 3


