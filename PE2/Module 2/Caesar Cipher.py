import time

def encrypt(text):
    # Caesar cipher - encrypting a message
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    return cipher


def decrypt(cipher):
    # Caesar cipher - decrypting a message.
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)
    return text


print('----------CAESAR CIPHER----------')
running = True
while running:
    time.sleep(1)
    action = int(input('1) Encryption\n2) Decryption\n3) Close\n'))
    match action:
        case 1:
            txt = input('Enter text for encryption\n')
            print('encrypting', end='')
            for i in range(5):
                print('.', end=' ')
                time.sleep(1)
            print(encrypt(txt))
            loop = int(input('1) Home\n2) Close\n'))
            match loop:
                case 1:
                    continue
                case 2:
                    break
        case 2:
            ciph = input('Enter text for decryption\n')
            print('decrypting', end='')
            for i in range(5):
                print('.', end=' ')
                time.sleep(1)
            print(decrypt(ciph))
            loop = int(input('1) Home\n2) Close\n'))
            match loop:
                case 1:
                    continue
                case 2:
                    break
        case 3:
            break
