# a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
a , b = 0, 0
while b <= blocks:
    height = a      # number of blocks per layer equals the height for a pyramid
    a += 1  # blocks per layer
    b += a  # total number of blocks used

print("The height of the pyramid:", height, sep=" ... ")
