# 👉 Async allows tasks to run without blocking, improving performance for I/O operations

import asyncio

async def download_file(file_name: str, delay: int):
    print(f"Starting download: {file_name}")
    await asyncio.sleep(delay)   # simulate network delay
    print(f"Finished download: {file_name}")
    return f"{file_name} downloaded"


async def main():

    # Run multiple downloads concurrently
    results = await asyncio.gather(
        download_file("file1.pdf", 2),
        download_file("file2.jpg", 3),
        download_file("file3.mp4", 1)
    )

    print("\nAll downloads completed.")
    print("Results:", results)


asyncio.run(main())


# 🧍 Async (Single person multitasking)

# 👉 One person:

# starts cooking 🍳
# while waiting → checks phone 📱
# while waiting → does another task

# 👉 Smart waiting

# 👨‍👩‍👦 Multithreading (Multiple people)

# 👉 3 people:

# one cooks 🍳
# one cleans 🧹
# one shops 🛒

# 👉 Work happens truly in parallel

# 👉 In async, when one task waits (await), other tasks continue running