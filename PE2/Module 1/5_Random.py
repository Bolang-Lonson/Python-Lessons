from random import random

for i in range(5):
    print(random())     # produces a float number x coming from the range (0.0, 1.0)

#########################################
from random import random, seed

seed(0) # sets seed as 0, seed() sets seed as current time

for i in range(5):
    print(random())

########################################
#   randrange(end)
#   randrange(beg, end)
#   randrange(beg, end, step)
#   randint(left, right) - it generates the integer value i, which falls in the range [left, right] (no exclusion on the right side).
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
