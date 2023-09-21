"""
time.struct_time:
    tm_year   # specifies the year
    tm_mon    # specifies the month (value from 1 to 12)
    tm_mday   # specifies the day of the month (value from 1 to 31)
    tm_hour   # specifies the hour (value from 0 to 23)
    tm_min    # specifies the minute (value from 0 to 59)
    tm_sec    # specifies the second (value from 0 to 61 )
    tm_wday   # specifies the weekday (value from 0 to 6)
    tm_yday   # specifies the year day (value from 1 to 366)
    tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # specifies the offset east of UTC (value in seconds)
"""
"""
The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.
"""
import time

timestamp = 1572879180
print(time.gmtime(timestamp))   #   For the gmtime function, the tm_isdst attribute is always 0.
print(time.localtime(timestamp))

""" The time module has functions that expect a struct_time object or a tuple that stores values according to the indexes presented when discussing the struct_time class."""
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))) #   converts a time_struct object to timestamp 
