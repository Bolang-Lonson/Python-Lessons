from sys import path

path.append("/Users/annie/Documents/Dev/Python-Lessons/PE2/Module 1/Exprmt")
print(path[-1])  # Check if the path was added correctly

from module import suml, prodl
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

