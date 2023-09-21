""" Searches the sequence from the beginning, in order to find the first element of the value specified in its argument
Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception."""

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
print("aAbByYzZaA".index("a"))
# Demonstrating the list() function:
smpl = "abcabc"
print(list(smpl))

# Demonstrating the count() method:
print(smpl.count("b"))
print(smpl.count("d"))

#######################
