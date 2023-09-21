def showTime(h, m, s):
    if s >= 60:
        m += 1
        s %= 60
        if m >= 60:
            h += 1
            m %= 60
    h %= 24
    h_str = ''
    if h < 10:
        h_str = '0' + str(h)
    else:
        h_str = str(h)

    m_str = ''
    if m < 10:
        m_str = '0' + str(m)
    else:
        m_str = str(m)
    s_str = ''
    if s < 10:
        s_str = '0' + str(s)
    else:
        s_str = str(s)

    return h_str + ':' + m_str + ':' + s_str

class Timer:
    def __init__(self, hrs=0, mins=0, secs=0):
        self.__hour = hrs
        self.__mins = mins
        self.__secs = secs

    def __str__(self):
        return showTime(self.__hour, self.__mins, self.__secs)

    def next_second(self):
        self.__secs += 1

    def prev_second(self):
        self.__secs -= 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
