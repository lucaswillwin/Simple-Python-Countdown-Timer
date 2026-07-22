import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0, -1): # Counts down from time to 0
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = x // 3600
    print(f'{hours:02}::{minutes:02}:{seconds:02}') # Uses 0 padding so things like 9  become 09
    time.sleep(1)
print("Times Up")
