# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

first_half = my_list[:3]
print(first_half)
second_half = my_list[3:]
print(second_half)
copylist = my_list
del my_list[2:4]
print("after deleting some elements ", my_list)
print(copylist)
