import threading
import time
import random

buffer = []
BUFFER_SIZE = 100

pair_id = 0


def producer(machine_id):
    global pair_id

    while True:

        current = pair_id
        pair_id += 1

        p1 = f"M{machine_id}-{current}-P1"
        p2 = f"M{machine_id}-{current}-P2"

        if len(buffer) >= BUFFER_SIZE:
            print("The producing machine is broken")
            return

        buffer.append(p1)

        time.sleep(random.uniform(0, 0.01))

        if len(buffer) >= BUFFER_SIZE:
            print("The producing machine is broken")
            return

        buffer.append(p2)

        time.sleep(random.uniform(0, 0.01))


def consumer():
    while True:

        if len(buffer) < 2:
            print("The packaging machine is broken")
            return

        item1 = buffer.pop(0)
        item2 = buffer.pop(0)

        pair1 = "-".join(item1.split("-")[:2])
        pair2 = "-".join(item2.split("-")[:2])

        if pair1 != pair2:
            print("Pairs are incorrect")
            return

        time.sleep(random.uniform(0, 0.01))


for i in range(3):
    threading.Thread(target=producer, args=(i + 1,), daemon=True).start()

threading.Thread(target=consumer, daemon=False).start()
