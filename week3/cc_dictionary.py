inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


sum1 = sum(inches_snow[item] for item in inches_snow)
print("Total snowfall inches:", sum1)

snowfall = input("How many inches of snow fell on Thursday?")
snowfalls = int(snowfall)

print("Total snowfall inches", snowfalls + sum1)
