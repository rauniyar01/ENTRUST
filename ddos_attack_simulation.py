import threading
import time

def memory_hog():
    memory_hog_list = []
    try:
        while True:
            memory_hog_list.append(' ' * 10**6)  # Append 1MB of data continuously
            time.sleep(0.1)  # Slow down the allocation a little
    except MemoryError:
        print("Memory limit reached")
        #return #Stop further memory allocation

def cpu_hog():
    while True:
        pass  # Infinite loop to consume CPU cycles

# Launch multiple threads to simulate attack
threads = []
for _ in range(10):
    t = threading.Thread(target=memory_hog)
    threads.append(t)
    t.start()

for _ in range(5):
    t = threading.Thread(target=cpu_hog)
    threads.append(t)
    t.start()

# Keep the main program alive
for t in threads:
    t.join()