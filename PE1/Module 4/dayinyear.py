def year_is_leap(year):
    if year % 4 != 0:  # if the year number isn't divisible by four, it's a common year
        return False
    elif year % 100 != 0:  # otherwise, if the year number isn't divisible by 100, it's a leap year
        return True
    elif year % 400 != 0:  # otherwise, if the year number isn't divisible by 400, it's a common year
        return False
    else:  # otherwise, it's a leap year
        return True

def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year_is_leap(year):
            return 29
        else:
            return 28
    else:
        return None

def day_of_year(year, month, day):
    months = [m+1 for m in range(12)]
    day_num = 0
    for i in months[:month-1]:
        day_num += days_in_month(year, i)
    day_num += day
    return day_num

print(day_of_year(2023, 8, 22))
