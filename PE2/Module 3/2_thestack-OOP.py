class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.stack_list = []

stack_object = Stack()  # Instantiating the object.
print(len(stack_object.stack_list))

#   When any class component has a name starting with two underscores (__), it becomes private -
#   this means that it can be accessed only from within the class.
class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))
