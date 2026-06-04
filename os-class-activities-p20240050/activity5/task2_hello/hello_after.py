import threading

after_e = threading.Semaphore(0)
after_l1 = threading.Semaphore(0)
after_l2 = threading.Semaphore(0)


def process1():
    print("H", end="")
    print("E", end="")
    after_e.release()


def process2():
    after_e.acquire()

    print("L", end="")

    after_l1.release()
    after_l1.acquire()

    print("L", end="")

    after_l2.release()


def process3():
    after_l2.acquire()
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
