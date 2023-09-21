from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
#   creates a timedelta object of timedelta class in datetime module
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
""" arguments are: days, seconds, microseconds, milliseconds, minutes, hours, and weeks."""
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

