alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('******************The Letter Counter*******************')

while True:
    word = input('Enter your word:\n')
    for letter in word:
        print(letter, end='|\t')
        print('Pos:', (word.index(letter) + 1), end='\t')
        print('Freq:', word.count(letter))
        print('**************************************************')
    loop = input('Continue? yes or no\n')
    if loop in 'NnNonoNOnO':
        print('End')
        break

#
#   Creating alphabet of cap letters
#
alf = 'A'
for i in range(25):
    nxt = chr(ord(alf[i]) + 1)
    alf += nxt

print(alf)
print(alf.lower() == alphabet)
