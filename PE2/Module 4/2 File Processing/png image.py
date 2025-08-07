from os import strerror

srcname = input("Enter file name ")

try:
    file = open(srcname, 'rb')
    image = bytearray(file.read())
    newfile = open("C:/Users/New User/OneDrive/Desktop/new image.jpg", 'wb')
    newfile.write(image)
    file.close()
    newfile.close()

except IOError as err:
    print("Error", strerror(err.errno))
