from os import strerror

srcname = input("Enter file name ")
occur = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

try:
    txt = open(srcname, 'rt')
    content = txt.read()
    for ch in content:
        if ch.isalpha():
            occur[ch.lower()] += 1

    for k in occur.keys():
        if occur[k] > 0:
            print(f'{k} -> {occur[k]}')
    txt.close()
except IOError as err:
    print("Error", strerror(err.errno))
