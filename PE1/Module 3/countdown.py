import time
print(
    """ StopWatch
        0 0 : 0 0
    """
)
time.sleep(2)
dur = int(input("Enter the duration in seconds: \nHit Enter to start\n"))
for i in range(dur,-1,-1):
    print(i)
    time.sleep(1)

