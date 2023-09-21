# Demonstrating the ord() function.
# If you want to know a specific character's ASCII/UNICODE code point value
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))  # The function needs a one-character string as its argument
print(ord(char_2))
# Demonstrating the chr() function.

print(chr(97))  # The function takes a code point and returns its character.
print(chr(945))
'''
chr(ord(x)) == x
ord(chr(x)) == x
'''
