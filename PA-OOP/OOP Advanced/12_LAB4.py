"""Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored."""

from datetime import datetime

def print_time(function):

    def wrapper(*args, **kwargs):
        st = datetime.now()
        print()
        print(st.strftime("%Y-%m-%d %H:%M:%S"))
        
        return function(*args, **kwargs)

    return wrapper
    

@print_time
def hello():
    print("Hello from simple function")

@print_time
def add(a, b):
    return a + b

@print_time
def mult(a, b):
    return a * b

hello()
print("Result is:", add(434, 859))
print("Result is:", mult(434, 859))