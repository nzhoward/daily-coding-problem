from threading import Thread
import time
from datetime import datetime as dt


def delayed(f, ms):
    time.sleep(ms)
    return f()


def hello(name):
    print(name, dt.now())


job1 = Thread(target=delayed, args=(lambda: hello('hello1'), 2))
job2 = Thread(target=delayed, args=(lambda: hello('hello2'), 1))

print(dt.now())
job2.start()
job1.start()
