income = float(input("Enter the annual income: "))

if income > 85528:
    surplus = income - 85528 # introducing surplus
    tax=14839.02+(0.32*surplus)
else:
    tax=(0.18*income)-556.02
#
# Write your code here.
# no negative tax
if tax<0:
    tax=0.0
#
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
