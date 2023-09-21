secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
resp = int(input("Number: "))
while resp!= secret_number:
    print("Ha ha! You're stuck in my loop!")
    resp = int(input("Number: "))
#if number is correct
print(secret_number,"Well done, muggle! You are free now.",sep="\n")
