#Using the Gregorian system
#requesting year input
year=int(input("Enter the year: "))

#defining the various year types as yt1 and yt2
yt1="Leap year" 
yt2="Common year"
# Gregorian year 1582
if year > 1582:
    if year%4 != 0: #if the year number isn't divisible by four, it's a common year
        yeartype=yt2
    elif year%100 != 0: #otherwise, if the year number isn't divisible by 100, it's a leap year
        yeartype=yt1
    elif year%400 != 0: #otherwise, if the year number isn't divisible by 400, it's a common year
        yeartype=yt2
    else: #otherwise, it's a leap year
        yeartype=yt1
    print(yeartype)
else: #years before Greg year 1582
    print("Not within the Gregorian calendar period")
