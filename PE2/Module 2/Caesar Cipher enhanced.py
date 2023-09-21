from time import sleep
import math

def encrypt(text, shift=1):
    code = ''
    for ch in text:
        if ch.isalpha():
            newOrd = ord(ch) + shift
            upperBound = [ord('A'), ord('a')]
            lowerBound = [ord('Z'), ord('z')]
            if newOrd > lowerBound[0] >= ord(ch):
                code += chr((newOrd - lowerBound[0]) - 1 + upperBound[0])
            elif newOrd > lowerBound[1] >= ord(ch):
                code += chr((newOrd - lowerBound[1]) - 1 + upperBound[1])
            else:
                code += chr(newOrd)
        
        else:
            code += ch
    
    return code

print("-------------CAESAR CIPHER 2.0--------------")
while True:
    txt = input('Enter line to be encrypted\n')
    sh = int(input('Shift(0-25): '))
    if sh <= 25:
        print('Encrypting', end=' ')
        for timr in range(int(round(math.sqrt(len(txt)), 0))):     # delay based on length of line
            sleep(1)
            print('.', end=' ')

        sleep(1)
        print(encrypt(txt, sh))
    else:
        print('Shift value must be from 0 to 25!')
        continue
    loop = int(input('1) Home\n2) Close\n'))
    match loop:
        case 1:
            continue
        case 2:
            break
