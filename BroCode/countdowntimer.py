import time

my_time = int(input("Enter the time in secs: "))
# time.sleep(my_time)

# for x in reversed(range(0,my_time)):
for x in range(my_time, 0, -1):
    secs = x % 60
    mins = int(x/60) %60
    hours = int(x/3600)
    print(f"{hours:02}:{mins:02}:{secs:02}") # 2 digits, use 0 as padding
    time.sleep(1)

print("Time's Up!")
