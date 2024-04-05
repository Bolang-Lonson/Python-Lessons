def simple_hello():
    print("Hello from simple function!")

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


decorator = simple_decorator(simple_hello)
decorator()

"""With some syntactic sugar"""

def decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

@decorator
def hello():
    print('Hello from simple function')

hello()
"""the name of the simple_function object ceases to indicate the object representing our simple_function() and from that moment on it indicates the object returned by the decorator, the simple_decorator."""