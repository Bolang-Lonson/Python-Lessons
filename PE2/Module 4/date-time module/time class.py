""" time(hour, minute, second, microsecond, tzinfo, fold)"""
#   The tzinfo parameter is associated with time zones, while fold with wall times.
from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
