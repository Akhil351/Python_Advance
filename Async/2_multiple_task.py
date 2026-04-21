import asyncio


# Task 1: API Call
async def api_call():
    print("Fetching API data...")
    await asyncio.sleep(3)
    print("API data fetched")


# Task 2: Data Processing
async def process_data():
    print("Processing data...")
    await asyncio.sleep(5)
    print("Data processed")


# Task 3: Save to Database
async def save_data():
    print("Saving data...")
    await asyncio.sleep(2)
    print("Data saved")


async def main():

    await asyncio.gather(
        api_call(),
        process_data(),
        save_data()
    )

    print("\nAll tasks completed.")


asyncio.run(main())