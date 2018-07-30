import threading

def worker_1():
    # get the name of current thread
    print(threading.current_thread().getName())
    print("Worker_1 initialized...")

    for i in range(1,10000):
        for j in range(1,1000):
            i + j

    print("Worker_1 finised...")

def worker_2():
    print(threading.current_thread().getName())
    print("Worker_2 initialized...")

    for i in range(1, 100):
        for j in range(1, 100):
            i + j

    print("Worker_2 finised...")

# worker_1()
# worker_2()

thread_1 = threading.Thread(target=worker_1)
thread_2 = threading.Thread(target=worker_2)

thread_1.start()
thread_2.start()