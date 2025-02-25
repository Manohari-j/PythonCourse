import datetime

date = datetime.date(2025, 2, 20)  # Year-month-date
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(12,30,5)  # hours, min, sec
now = datetime.datetime.now()
# to customize the format
now = now.strftime("%H:%M:%S %m-%d-%Y")
print(time)
print(now)

target = datetime.datetime(2030,1,2,12,30,1)
current = datetime.datetime.now()

now = target.strftime("%H:%M:%S %m-%d-%Y")
print(now)

if target < current:
    print("Target date has passed")
else:
    print("Target date has not passed")