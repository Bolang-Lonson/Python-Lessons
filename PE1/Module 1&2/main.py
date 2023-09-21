hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
end_hour = hour + (dura // 60)  # If duration is over 60 mins it counts as an hour, if not it's zero
if (mins + dura % 60) >= 60:  # remainder of duration with 60 mins ie. itself if less than 60
    end_hour += 1
    end_mins = (mins + dura % 60) % 60  # since the 60 mins was converted to an hour we use the remainder
else:
    end_mins = mins + dura % 60
#       Printing end time in hour:min format
print("Event ends at "+ str(end_hour % 24) + ":" + str(end_mins))  # 24h format
