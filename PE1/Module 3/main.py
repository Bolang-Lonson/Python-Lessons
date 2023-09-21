# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = max(number1, number2, number3)
smallest_number=min(number3, number2, number1)
# print the result
print("The largest number is:", largest_number,"\nThe smallest number is:", smallest_number)
