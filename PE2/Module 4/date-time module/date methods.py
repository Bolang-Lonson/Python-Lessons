from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

""" weekday method returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. """
print(d.weekday())

""" isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday:"""
d = date(2019, 11, 4)
print(d.isoweekday())
