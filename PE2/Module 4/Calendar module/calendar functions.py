import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)
print(calendar.weekday(2023, 2, 26))

print(calendar.weekheader(2))   #   Result: Mo Tu We Th Fr Sa Su.  the argument is how long the abbreviation is

""" The first one, called isleap, returns True if the passed year is leap, or False otherwise. 
The second one, called leapdays, returns the number of leap years in the given range of years."""
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2023))  # Up to but not including 2023.
