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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

switch = 1
while switch:
    m = int(input("Enter month:\n"))
    y = int(input("Enter year:\n"))
    print("Number days in month are ", days_in_month(y,m))
    resp = None
#   To continue loop
    while resp not in ["N","Y"]:
        resp = input("Continue? Y or N\n").upper()
        if resp not in ["N","Y"]:
            print("Unknown response")
    if resp == "Y":
        switch = 1
    elif resp == "N":
        switch = 0

print("Ended")
