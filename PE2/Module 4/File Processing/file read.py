from os import strerror

try:
    cnt = 0
    s = open('/Users/annie/Documents/Dev/Python Lessons/PE2/Module 4/File Processing/file write and read.py', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

######################################################### OR ####
try:
    cnt = 0
    s = open('/Users/annie/Documents/Dev/Python Lessons/PE2/Module 4/File Processing/file write and read.py', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
