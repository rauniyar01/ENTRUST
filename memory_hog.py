import time

# Allocate a large amount of memory
memory_hog = []

try:
    while True:
        memory_hog.append(' ' * 10**6)  # Append data to the list continuously
        time.sleep(0.1)  # Sleep to slow down the allocation a bit
except MemoryError:
    print("Memory limit reached")
