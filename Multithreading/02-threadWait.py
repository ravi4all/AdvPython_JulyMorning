import threading, time

def worker():
    name = threading.current_thread().getName()
    print("Thread {} enters".format(name))

    seconds = 10
    while seconds > 0:
        seconds -= 1
        time.sleep(0.5)

    print("Thread {} exits".format(name))

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()