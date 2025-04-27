'''Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
to add an integer to a time interval object means to add seconds;
to subtract an integer from a time interval object means to remove seconds.
'''

class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add_sub(self, other, operation_type: str):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds

        if operation_type == 'subtraction':
            new_time = own - another
        elif operation_type == 'addition':
            new_time = own + another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
    
    def __int_add_sub(self, other: int, op: str):
        '''new method added to handle integer second addition and subtraction'''
        own = self.hours * 3600 + self.minutes * 60 + self.seconds

        if op == 'sub':
            new_time = own - other
        elif op == 'add':
            new_time = own + other
        else:
            raise Exception('Unknow operation')
        
        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60

        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'addition')
        elif isinstance(other, int):
            return self.__int_add_sub(other, 'add')
        else:
            raise TypeError('can only add TimeInterval or Integer (seconds) objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        elif isinstance(other, int):
            return self.__int_add_sub(other, 'sub')
        else:
            raise TypeError('can only subtract TimeInterval or Integer (seconds) objects')

    def __mul__(self, other):
        if isinstance(other, int):
            new_time = (self.hours * 3600 + self.minutes * 60 + self.seconds) * other
            new_hours = new_time // 3600
            new_minutes = (new_time % 3600) // 60
            new_seconds = new_time % 60
            return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)
        else:
            raise TypeError('can only multiply TimeInterval objects by integers')

    def __str__(self):
        return "%s:%s:%s" % (self.hours, self.minutes, self.seconds)
    

t1 = TimeInterval(hours=11, minutes=53)
t2 = TimeInterval(hours=2, minutes=30, seconds=10)

print(t1 + 7200)