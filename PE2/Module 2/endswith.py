"""
The endswith() method checks if the given string ends with the specified argument ie substring and returns True or False, depending on the check result.
"""
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
#################################
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

#   The find() method
"""it looks for a substring and returns the index of first occurrence of this substring"""
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
#   returns 1 if successful and -1 if not
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
#   rfind() starts from the right instead
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))  # slices from second argument
