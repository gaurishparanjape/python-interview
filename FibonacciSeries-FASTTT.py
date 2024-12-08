from functools import lru_cache

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n)
def fibonaccicall(n):
    for i in range(1,n+1):
        print(fibonacci(n))

fibonaccicall(10)