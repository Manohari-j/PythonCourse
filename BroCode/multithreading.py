# to perform multiple tasks concurrently - multitasking
# Good for I/O bound tasks like reading files, fetching data from APIs
# threading.Thread(target = func)

import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking the dog {first}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# if it's a tuple and has only one element add a comma.

t1 = threading.Thread(target=walk_dog, args=("Pluto",))
t1.start()
t2 = threading.Thread(target=take_out_trash())
t2.start()
t3 = threading.Thread(target=get_mail)

t3.start()
print(threading.active_count())
print(threading.enumerate())
t1.join()
t2.join()
t3.join()


print("All chores are completed")
