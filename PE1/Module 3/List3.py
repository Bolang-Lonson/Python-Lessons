i = 0
vect: list[str] = []
elt: str = ""
print("Input elements of list\nOr type 'end'/'End'/'END' to stop\n")
while elt not in ["end", "End", "END"]:
    if elt != "":
        vect.insert(i,elt)
        i+=1
    elt = input().upper()

print("List of elements:", vect, sep="\n")
print(f'{len(vect)} elements!')
