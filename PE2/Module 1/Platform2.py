from platform import python_implementation, python_version_tuple, win32_ver

print(python_implementation())  # python_implementation() → returns a string denoting the Python implementation
# python_version_tuple() → returns a three-element tuple filled with:
# ->the major part of Python's version;
# ->the minor part;
# ->the patch level number.
for atr in python_version_tuple():
    print(atr)
print(win32_ver())
