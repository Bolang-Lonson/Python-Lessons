""" open(filename, mode=open_mode, encoding=text_encoding)"""
from os import strerror

try:
    stream = open("C:/Users/User/Desktop/file.txt", "rt")
    # Processing goes here.
    stream.close()

except IOError as exc:
    print(exc.errno)
    print("Which means", strerror(exc.errno))
except Exception as exc:
    print("Cannot open the file:", exc)
