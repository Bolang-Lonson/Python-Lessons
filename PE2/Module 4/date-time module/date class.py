from datetime import date

today = date.today()    #   Be careful, because these attributes are read-only

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

""" To create a date object, you must pass the year, month, and day parameters as follows:"""
my_date = date(2019, 11, 4)
print(my_date)
