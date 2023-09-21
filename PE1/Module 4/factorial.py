def factorial(n):
    if n < 0:
        return
    if n < 2:
        return 1

    pdt = 1
    for i in range(2, n+1):
        pdt*=i
    return pdt

print("The factorial of ")
for n in range(1,6):
    print(n, "is", factorial(n))
