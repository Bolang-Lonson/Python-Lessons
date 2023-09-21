import os

os.mkdir("my_first_directory")
print(os.listdir())
""" The listdir function returns a list containing the names of the files and directories that are in the path passed as an argument.
If no argument is passed to it, the current working directory will be used"""
######## Recursive Directories #########
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
