from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, ["A", "B", "C"])