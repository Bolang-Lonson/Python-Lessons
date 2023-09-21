""" The object returned by the open() function is an instance of the iterable class
its __next__ method just returns the next line read in from the file."""
from os import strerror

try:
    ccnt = lcnt = 0
    for line in open("./text.txt",'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I\O error occurred: ", strerror(e.errno))
