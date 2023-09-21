from sys import path

for p in path:
    print(p)
#   path.append('..\\Module 1\\Exprmt')
path.insert(1,'C:\\Users\\New User\\OneDrive\\Desktop\\Python Lessons\\PE2\\Module 1\\Exprmt')
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
