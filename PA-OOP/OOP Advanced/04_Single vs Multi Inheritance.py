'''In the multiple inheritance scenario, any specified attribute is searched for first in the current class. If it is not found, the search continues into the direct parent classes in depth-first level (the first level above), from the left to the right, according to the class definition. This is the result of the MRO algorithm.'''

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

class E(C, B):
    pass


D().info()
E().info()
# Python finds the requested method in the class B definition and stops searching



'''MRO inconsistency'''
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(A, C):
    pass

D().info()
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C