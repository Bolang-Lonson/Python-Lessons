
# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
print("Now enter the members Stu Sutcliffe and Pete Best")
for i in range(2):
    beatles.append(input())
print("Step 3:", beatles)

# step 4
for n in range(4,2,-1):
    del beatles[n]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))
for member in beatles:
    print(member, end=", ")
