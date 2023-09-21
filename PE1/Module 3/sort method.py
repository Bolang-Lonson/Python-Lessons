my_list = []
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = (input("Enter a list element: "))
    my_list.append(val)

my_list.sort()
print("\nSorted:")
print(my_list)
