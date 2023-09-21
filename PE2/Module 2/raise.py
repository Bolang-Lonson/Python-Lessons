def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
#############################################
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise       # when used without specifying the exception can only be done inside a try-except block

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
