def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    # fib(n) = fib(n-1) + fib(n-2)
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(0, 11):  # testing
    print("fib("+str(n)+")", "->", fib(n))


# Memorised version of the fibonacci
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

print(fibonacci(25))