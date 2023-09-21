""" you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception)"""
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

for b in data:
    print(hex(b))
