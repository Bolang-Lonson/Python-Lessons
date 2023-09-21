my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length//2):
    my_list[i], my_list[-i-1] = my_list[-i-1], my_list[i]
# when i=0, -i-1=-1 hence indexing last element of list
# i=1, -i-1=-2 hence indexing second to last element and so on
print(my_list)

# OR
my_list.reverse()
print(my_list)
