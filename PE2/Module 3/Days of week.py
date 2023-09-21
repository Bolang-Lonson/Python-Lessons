class WeekDayError(Exception):
    pass


class Weeker:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in Weeker.days:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        day_num = Weeker.days.index(self.__day)
        day_num += n
        day_num %= 7
        self.__day = Weeker.days[day_num]

    def subtract_days(self, n):
        day_num = Weeker.days.index(self.__day)
        day_num -= n
        day_num %= 7
        self.__day = Weeker.days[day_num]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
