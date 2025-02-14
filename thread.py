import threading
import time


def update_db():
    print("Updating db...")
    time.sleep(5)  # forcing a delay in secs
    print("Updated the db")


def display_nums(num):
    for i in range(1, num + 1):
        print(i)


# update_db()

t1 = threading.Thread(target=update_db)
t1.start()
display_nums(25)
print(threading.active_count())
print(threading.enumerate())  # to know what thread is running

t1.join()
print("Bye")  # stop from printing before all threads complete use join to finish the thread
