# A function that checks whether a list passed as an argument contains
# nine digits from '1' to '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    row = input()
    rows.append(row)
ok = True

# Check if all rows are good.
for r in range(9):
    for l in range(9):
        if rows[r][l] in rows[r][l+1:]:
            ok = False

# Check if all columns are good.
if ok:
    for c in range(9):
        for w in range(9):
            if rows[c][w]

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):


# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
