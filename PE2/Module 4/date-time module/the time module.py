import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

""" ctime, which converts the time in seconds since January 1, 1970 (Unix epoch) to a string."""
timestamp = 1572879180
print(time.ctime(timestamp))

""" without passing any time arguments"""
print(time.ctime())
