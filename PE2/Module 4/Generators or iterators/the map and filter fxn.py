"""  The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results."""
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

""" filters its second argument while being guided by directions flowing from the function specified as the first argument
The elements which return True from the function pass the filter - the others are rejected."""
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
