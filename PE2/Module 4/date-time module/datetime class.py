""" datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)"""
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

""" The datetime class has several methods that return the current date and time. These methods are:"""

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

""" Can convert a datetime object to a timestamp using a method"""
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())
