from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"Task {name} is running")


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")
    executor.submit(task, "C")
    
# 👉 ThreadPoolExecutor is used to run multiple tasks concurrently using a pool of threads