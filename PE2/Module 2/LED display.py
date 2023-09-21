segmt = [['#' for i in range(3)] for j in range(5)]

def splice(number):
    str_list = []
    ch = ''
    for i in range(5):
        for j in range(3):
            ch += number[i][j]      #   creating a list of strings of each spliced line
            ch += ' '
        str_list.append(ch)
        ch = ''

    return str_list

def display(number, ln):
    strout = splice(number)        # I could actually merge both functions
    return strout[ln]

#   creating pattern for 1
one = [elt[:] for elt in segmt]
for m in range(5):
    for n in range(2):
        one[m][n] = ' '  # one[m][n].replace('#',' ', 1)
#   0 pattern
zero = [elt[:] for elt in segmt]
for x in range(1, 4):
    zero[x][1] = ' '
#   2 pattern
two = [elt[:] for elt in segmt]
two[1][0] = two[1][1] = two[3][1] = two[3][2] = ' '
#   3 pattern
three = [elt[:] for elt in segmt]
for y in [1, 3]:
    for x in range(2):
        three[y][x] = ' '
#   4 pattern
four = [elt[:] for elt in segmt]
for y in range(2):
    four[y][1] = ' '
for z in range(3, 5):
    for x in range(2):
        four[z][x] = ' '
#   5 pattern
five = [elt[:] for elt in segmt]
i = 2
for f in [1, 3]:
    i -= 1
    for fi in range(2):
        five[f][fi + i] = ' '
#   6 pattern
six = [elt[:] for elt in segmt]
nn = [1,2]
for s in [1,3]:
    for ix in nn:
        six[s][ix] = ' '
    del nn[-1]
#   7 pattern
seven = [elt[:] for elt in segmt]
for e in range(1,5):
    for ev in range(2):
        seven[e][ev] = ' '
#   8 pattern
eight = [elt[:] for elt in segmt]
for g in [1,3]:
    eight[g][1] = ' '
#   9 pattern
nine = [elt[:] for elt in segmt]
j = [1]
for n in [1,3]:
    for ni in j:
        nine[n][ni] = ' '
    j.insert(0,0)


num_ref = {
    0: zero, 1: one, 2: two, 3: three, 4: four,
    5: five, 6: six,7: seven, 8: eight, 9: nine
}

###########################################
print('---------------LED SEGMENT DISPLAY-----------------')
running = True
while running:
    val = (input('Enter number to display\n'))
    line = ''
    screen = []
    for ln in range(5):
        for digit in val:
            digit = int(digit)
            output = num_ref[digit]
            line += display(output, ln) + ' '
        screen.append(line)
        line = ''

    for output_line in screen:
        print(output_line)
    cont = input('\nY) Continue\nN) End\n')
    match cont:
        case 'Y':
            continue
        case 'y':
            continue
        case 'N':
            break
        case 'n':
            break

print('End')