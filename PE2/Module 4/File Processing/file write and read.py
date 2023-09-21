import errno
from os import strerror

try:
    stream = open("C:/Users/New User/OneDrive/Desktop/Python Lessons/PE2/Module 4/File Processing/stream open.py", "at")
    stream.write("\"\"\"Pussy ass niggas \n Everywhere\"\"\"")
    stream.close()
    stream = open("C:/Users/New User/OneDrive/Desktop/Python Lessons/PE2/Module 4/File Processing/stream open.py", "rt")
    print(stream.read())
    stream.close()

except IOError as er:
    print("Error", strerror(er.errno))
