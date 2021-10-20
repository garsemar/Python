import threading
import time


def breakfast():
    time.sleep(3)
    print("You breakfast")


def cofee():
    time.sleep(4)
    print("Cofee")


def study():
    time.sleep(5)
    print("You study")


x = threading.Thread(target=breakfast, args=())
x.start()

y = threading.Thread(target=cofee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())