class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

"""The self parameter is also used to invoke other object/class methods from inside the class."""
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()

class Nonesense:
    def __init__(self, value=None):
        self.var = value

obj1 = Nonesense("object")
obj2 = Nonesense()
print(obj1.var)
print(obj2.var)
###################################
"""__module__ is a string, too - it stores the name of the module which contains the definition of the class."""
class Classy:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)
