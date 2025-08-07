class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'My name is ' + self.name + '.'

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj = Sub('Andy')
print(obj)

# OR
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'My name is ' + self.name + '.'

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)
# you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.
obj = Sub('Andy')
print(obj)
