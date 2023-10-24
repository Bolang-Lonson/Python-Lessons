class Demo:
    def __init__(self, value):
        self.instance_var = value

    class_var = 'shared variable'

d1 = Demo(100)
d2 = Demo(200)

# instance variables can be created during any moment of an object's life
d1.another_var = 'another variable in the object'

print('contents of d1:', d1.__dict__)
print('contents of d2:', d2.__dict__)

"""A class variable is a class property that exists in just one copy, and it is stored outside any class instance. Because it is owned by the class itself, all class variables are shared by all instances of the class. They will therefore generally have the same value for every instance; butas the class variable is defined outside the object, it is not listed in the object's __dict__."""

print(Demo.class_var)
print(Demo.__dict__)
print(d1.class_var)
print(d2.class_var)