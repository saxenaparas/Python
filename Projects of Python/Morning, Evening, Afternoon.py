import time
timestamp = time.strftime('%H:%M:%S') # Remember: output is [string] not [integer]
print(timestamp)
Hour = time.strftime('%H')
print(Hour)

if Hour >= 0 and Hour < 12:
    print("Good Morning Sir!")
elif Hour >= 12 and Hour < 17:
    print("Good Afternoon Sir!")
elif Hour >= 17 and Hour < 0:
    print("Good Night Sir!")
else:
    print("Good Evening Sir!")