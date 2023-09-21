from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self):
        Calendar.__init__(self)

    def count_weekday_in_year(self, year, weekday):
        count = 0
        for i in range(1, 13):
            for mn in self.monthdays2calendar(year, i):
                for wk in mn:
                    if wk[1] == weekday and wk[0] != 0:
                        count += 1

        return count


testcal = MyCalendar()
print(testcal.count_weekday_in_year(2000, 6))
