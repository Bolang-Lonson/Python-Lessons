print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

#   Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
#   The centering is actually done by adding some spaces before and after the string
#   If the target field's length is too small to fit the string, the original string is returned.
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
#   with 2 arguments it uses the 2nd as a filler

print('[' + 'gamma'.center(20, '*') + ']')
