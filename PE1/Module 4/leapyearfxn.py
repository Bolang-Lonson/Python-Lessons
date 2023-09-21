def is_year_leap(year):

    if year % 4 != 0:  # if the year number isn't divisible by four, it's a common year
        is_leap = False
    elif year % 100 != 0:  # otherwise, if the year number isn't divisible by 100, it's a leap year
        is_leap = True
    elif year % 400 != 0:  # otherwise, if the year number isn't divisible by 400, it's a common year
        is_leap = False
    else:  # otherwise, it's a leap year
        is_leap = True
    return is_leap


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
