import time
import multiprocessing

def cpu_bound():
    while True:
        pass

if __name__ == '__main__':
    # Start multiple CPU-bound tasks to stress the CPU
    num_processes = multiprocessing.cpu_count()
    processes = [multiprocessing.Process(target=cpu_bound) for _ in range(num_processes)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
