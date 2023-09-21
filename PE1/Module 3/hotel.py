days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

calendar = [[day for day in days] for week in range(4)]
print(calendar)
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14
rooms[1][9][13] = True
# and release the second room on the fifth floor located in the first building
rooms[0][4][1] = False
# Vacancy chunk
# Check if there are any vacancies on the 15th floor of the third building
vacancy = 0
for room_num in range(20):
    if not rooms[2][14][room_num]:
        vacancy += 1
