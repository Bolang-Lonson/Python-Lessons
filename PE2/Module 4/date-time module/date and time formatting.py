from datetime import date, time, datetime

d = date.today()
print(d.strftime('%d-%m-%Y'))
#   anything can be used to separate the directives

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

