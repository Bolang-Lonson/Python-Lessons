'''A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.'''

import random

class Apple:
    count = 0
    totWeight = 0

    def __init__(self, weight):
        self.weight = weight
        Apple.totWeight += weight
        Apple.count += 1


while Apple.count < 1000 and Apple.totWeight < 300:
    apple = Apple(random.uniform(0.2, 0.5))

print('A limit has been reached. The order details:')
print('# of apples:', Apple.count)
print('total weight:', round(Apple.totWeight, 2))