squares = [x ** 2 for x in range(10)]
print("Squares:\n", squares)

odds = [x for x in squares if x % 2 != 0]
print("Odds:\n", odds)

evens = [x for x in squares if x % 2 == 0]  # OR if x not in odds
print("Evens:\n", evens)
