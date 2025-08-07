the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))  # parentheses make it a generator and not a list

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()
###################################################
for v in [1 if x % 2 == 0 else 0 for x in range(20)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(20)):
    print(v, end=" ")
print()
