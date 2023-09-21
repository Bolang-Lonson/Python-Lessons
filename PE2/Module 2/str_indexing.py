# Indexing strings.

the_string = 'silly walks'
copy = ''
for ix in range(len(the_string)):
    copy += the_string[ix]

print(copy)
print('copy equals original', copy==the_string)
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()
