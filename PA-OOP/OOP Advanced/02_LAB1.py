'''Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.'''
from datetime import time

class TimeInterval:
    def __init__(self, hours, minutes, seconds) -> None:
        self.time = time(hours, minutes, seconds)

    
    def __str__(self) -> str:
        # Objects created with time class from datetime module have a string formatting method strftime built-in
        return self.time.strftime('%H:%M:%S')
    

    def __add__(self, other):
        if isinstance(other, TimeInterval):
            h = self.time.hour + other.time.hour
            m = self.time.minute + other.time.minute
            s = self.time.second + other.time.second

            if s >= 60:
                m += (s // 60)
                s %= 60


            if m >= 60:
                h += (m // 60)
                m %= 60

            if h >= 24:
                h %= 24

            return TimeInterval(h, m, s)
        else:
            raise TypeError('can only add TimeInterval objects')
    

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            h = self.time.hour - other.time.hour
            m = self.time.minute - other.time.minute
            s = self.time.second - other.time.second

            return TimeInterval(h, m, s)
        else:
            raise TypeError('can only subtract TimeInterval objects')
    

    def __mul__(self, other: int):
        if isinstance(other, int):
            h = self.time.hour * other
            m = self.time.minute * other
            s = self.time.second * other

            if s >= 60:
                m += (s // 60)
                s %= 60


            if m >= 60:
                h += (m // 60)
                m %= 60

            if h >= 24:
                h %= 24

            return TimeInterval(h, m, s)
        else:
            raise TypeError('can only multiply TimeInterval objects by integers')
    

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti + sti)
print(fti - sti)
print(fti * 2)


"""My code above is less efficient than the suggested code below"""
class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add_sub(self, other, operation_type):
        own = self.hours * 3600 + self.minutes * 60 + self.seconds
        another = other.hours * 3600 + other.minutes * 60 + other.seconds   # Converting both times into seconds

        if operation_type == 'subtraction':
            new_time = own - another
        elif operation_type == 'addition':
            new_time = own + another
        else:
            raise Exception('Unknown operation')

        new_hours = new_time // 3600
        new_minutes = (new_time % 3600) // 60
        new_seconds = new_time % 60
        # Converting back to hours, minutes and seconds
        return TimeInterval(hours=new_hours, minutes=new_minutes, seconds=new_seconds)

    def __add__(self, other):
        if isinstance(other, TimeInterval): #   Condition for if operand is a TimeInterval Object
            return self.__add_sub(other, 'addition')
        else:
            raise TypeError('can only add TimeInterval objects')

    def __sub__(self, other):
        if isinstance(other, TimeInterval):
            return self.__add_sub(other, 'subtraction')
        else:
            raise TypeError('can only subtract TimeInterval objects')

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
    

t1 = TimeInterval(hours=21, minutes=58, seconds=50)
t2 = TimeInterval(1, 45, 22)

assert str(t1 + t2) == '23:44:12'
assert str(t1 - t2) == '20:13:28'
assert str(t1 * 2) == '43:57:40'

print('It works like a charm')
