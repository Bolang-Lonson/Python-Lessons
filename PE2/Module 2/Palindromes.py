def ispalindrome(text):
    text = text.replace(' ', '')
    text = text.lower()
    inverse = ''
    for ch in text:
        inverse = ch + inverse

    return text == inverse

print('Palindrome'.center(30, '-'))
while True:
    txt = input('Enter text\n')
    if ispalindrome(txt):
        print('It\'s a palindrome')
    else:
        print('It\'s not a palindrome')

    loop = int(input('1) Home\n2) Close\n'))
    match loop:
        case 1:
            continue
        case 2:
            break
