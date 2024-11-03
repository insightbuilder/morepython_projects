from prompt_toolkit.shortcuts import ProgressBar
import time
import threading

with ProgressBar() as pb:
    for i in pb(range(500)):
        time.sleep(0.01)

with ProgressBar() as pb:

    def task1():
        for _ in pb(range(100)):
            time.sleep(0.05)

    def task2():
        for _ in pb(range(150)):
            time.sleep(0.01)

    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task2)

    t1.daemon = True
    t2.daemon = True
    t3.daemon = True

    t1.start()
    t3.start()
    t2.start()

    for t in [t1, t2, t3]:
        while t.is_alive():
            t.join()
