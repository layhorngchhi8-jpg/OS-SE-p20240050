import threading
import random
import time


def process1():
    time.sleep(random.random())
    print("H", end="")
    time.sleep(random.random())
    print("E", end="")


def process2():
    time.sleep(random.random())
    print("L", end="")
    time.sleep(random.random())
    print("L", end="")


def process3():
    time.sleep(random.random())
    print("O", end="")


t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print()
