""" In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process."""

import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
print(os.listdir())
