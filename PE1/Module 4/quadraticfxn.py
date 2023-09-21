def quadratic(a,b,c):
    discriminant = (b**2) - (4*a*c)
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    roots = [x1, x2]
    return roots

print("Enter coefficients of the quadratic equation")
a1 = float(input("a:\n"))
b1 = float(input("b:\n"))
c1 = float(input("c:\n"))

x1 = quadratic(a=a1,b=b1,c=c1)[0]
x2 = quadratic(a1,b1,c1)[1]
print("Solutions are:\n",x1,x2)
