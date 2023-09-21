""" If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read."""
from os import strerror
data = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
""" Be careful - don't use this kind of read if you're not sure that the file's contents will fit the available memory."""
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

