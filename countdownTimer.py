#Countdown timer (For eggs!)

import time

eggType = int(input("What kind of egg do you want to make? \n 1. Soft-boiled (3 minutes), \n 2. Medium-boiled (5 minutes), or \n 3. Hard-boiled (7 minutes)? \n"))

if eggType == 1:
    start = 180
elif eggType == 2:
    start = 300
elif eggType == 3:
    start = 420
else:
    print("Invalid input. Please enter 1, 2, or 3.")
    exit()
print("Starting the timer for your egg...")
while start > 0:
    minutes = start // 60
    seconds = start % 60
    print(f"Time remaining: {minutes:02d}:{seconds:02d}")
    time.sleep(1)
    start -= 1
print("Your egg is ready! Enjoy!")