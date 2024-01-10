import threading
import time
import random


class Worker(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.tid = kwargs.pop("tid")
        self.data = kwargs.pop("data")
        self.running = False
        super().__init__(*args, **kwargs)

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        print(self.tid, "Worker Start")
        while self.running:
            if len(self.data) == 0:
                time.sleep(1)
                continue

            print(self.tid, "do", self.data.pop())

        print(self.tid, "Worker End")


if __name__ == "__main__":
    data = [random.randint(0, 100) for i in range(20)]
    workers = [Worker(tid=i, data=data) for i in range(10)]

    print("Start Worker")
    for w in workers:
        w.start()

    while (s := input("Enter data: ")).lower() != "end":
        data.append(s)

    for w in workers:
        w.stop()
        w.join()

    print("End Worker")
