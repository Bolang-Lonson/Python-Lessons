a=3.0
b=4.0
c=(a**2+b**2)**0.5
print("c=",c)
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


print(f'{miles} miles is {round(miles_to_kilometers, 2)} kilometers') # called an f-string