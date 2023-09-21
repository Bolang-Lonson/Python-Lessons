# Program: Collatz's hypothesis
c0 = int(input("Enter a positive non-zero number\n"))
count = 0
while c0 != 1:
    if c0 % 2 == 0:  # if it's even, evaluate a new c0 as c0 ÷ 2
        c0 //= 2
    else:           # otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1
        c0 = 3*c0 + 1
    count += 1
    print("c0: ", c0)
print("No of tries: ", count)
