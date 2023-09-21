def factorial(n):
    if n < 0:
        return
    if n < 2:
        return 1

    return factorial(n-1) * n

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print("25! = ", factorial(25), "\nwhile")
print("fib(25) = ", fib(25))

