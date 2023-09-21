""" a file opened in read mode will raise an error"""
from os import strerror
import sys

try:
    fo = open('newtext.txt', 'wt')  # A new file (newtext.txt) is created.
    for i in range(20):
        s = f"line # {str(i + 1)} \n"
        fo.write(s)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    sys.stderr.write(strerror(e.errno))
