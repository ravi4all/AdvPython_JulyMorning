import threading,time

def worker_1():
    name = threading.current_thread().getName()
    print("Thread {} enters".format(name))

    seconds = 10
    while seconds > 0:
        seconds -= 1
        time.sleep(0.5)

    print("Thread {} exits".format(name))

def worker_2():
    name = threading.current_thread().getName()
    print("Thread {} enters".format(name))

    seconds = 10
    while seconds > 0:
        seconds -= 1
        time.sleep(0.8)

    print("Thread {} exits".format(name))

t1 = threading.Thread(target=worker_1,
                      name="Non Daemon")

t2 = threading.Thread(target=worker_2,
                      name="Daemon")

t1.start()
# t1.setDaemon(True)
t2.setDaemon(True)
t2.start()

t2.join()