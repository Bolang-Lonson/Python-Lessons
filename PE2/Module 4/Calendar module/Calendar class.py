""" The Calendar class constructor takes one optional parameter named firstweekday, by default equal to 0 (Monday)."""
import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
""" As a result, all days in the specified month and year are returned, 
as well as all days before the beginning of the month or the end of the month that are necessary to get a complete week."""

for num in c.itermonthdays(2023, 2):
    print(num, end=' ')
"Prints numbers of the month for all days of the month"

for itr in c.itermonthdays2(2023, 2):
    print(itr, end=' ')
"Prints an integer tuple pair of day of the week and day of the month"
"""
itermonthdates3 – returns days in the form of tuples consisting of a year, a month, and a day of the month numbers.;
itermonthdates4 – returns days in the form of tuples consisting of a year, a month, a day of the month, and a day of the week numbers."""
