"""a method whose name starts with __ is (partially) hidden."""
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
""" the __name__ attribute is absent from the object - it exists only inside classes."""
print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)
#   The property contains the name of the class.
