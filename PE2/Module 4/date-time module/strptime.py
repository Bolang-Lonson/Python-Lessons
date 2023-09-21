from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))    #   as method
""" it creates a datetime object from a string representing a date and time."""

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))    #   as function
""" parses a string representing a time to a struct_time object."""
