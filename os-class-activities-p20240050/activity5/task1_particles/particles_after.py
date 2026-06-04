import threading
import time
import random
from collections import deque

buffer = deque()

produced_pairs = 0
packaged_pairs = 0
pair_counter = 0

empty_pairs = threading.Semaphore(50)
full_pairs = threading.Semaphore(0)
mutex = threading.Lock()

counter_lock = threading.Lock()


def producer(machine_id):
    global pair_counter
    global produced_pairs

    while True:

        with counter_lock:
            pid = pair_counter
            pair_counter += 1

        pair = (
            f"M{machine_id}-{pid}-P1",
            f"M{machine_id}-{pid}-P2"
        )

        empty_pairs.acquire()

        with mutex:
            buffer.append(pair)
            produced_pairs += 1

        full_pairs.release()

        time.sleep(random.uniform(0.05, 0.15))


def consumer():
    global packaged_pairs

    while True:

        full_pairs.acquire()

        with mutex:

            if len(buffer) == 0:
                print("The packaging machine is broken")
                return

            p1, p2 = buffer.popleft()

            pair1 = "-".join(p1.split("-")[:2])
            pair2 = "-".join(p2.split("-")[:2])

            if pair1 != pair2:
                print("Pairs are incorrect")
                return

            packaged_pairs += 1

            buffer_particles = len(buffer) * 2

        empty_pairs.release()

        print(
            f"Produced pairs: {produced_pairs} | "
            f"Packaged pairs: {packaged_pairs} | "
            f"Buffer particles: {buffer_particles}"
        )

        time.sleep(random.uniform(0.05, 0.15))


for i in range(3):
    threading.Thread(
        target=producer,
        args=(i + 1,),
        daemon=True
    ).start()

consumer()