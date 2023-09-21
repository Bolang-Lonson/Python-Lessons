from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))  # chooses a "random" element from the input sequence and returns it
print(sample(my_list, 5))   # the function chooses some input elements, returning a list with the choice.
print(sample(my_list, 10))  #  The elements in the sample are placed in random order.

