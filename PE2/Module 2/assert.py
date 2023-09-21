""" It evaluates the expression;
    if the expression evaluates to True, or a non-zero numerical value, or a non-empty string, or any other value different than None, it won't do anything else;
    otherwise, it automatically and immediately raises an exception named AssertionError (in this case, we say that the assertion has failed)
"""
import math

x = float(input("Enter a number: "))
assert x>= 0.0

x = math.sqrt(x)

print(x)
