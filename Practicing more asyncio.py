import asyncio
import random



async def student(id,sleep_time):
    "Hello ma'am can I please have some food for lunch?"
    ordering = asyncio.create_task(lunchLady())
    await ordering
    print(f"Thank you! I now have some {ordering}")

async def lunchLady():
    food = "Nothing"
    print("Sure, give me one moment")
    await asyncio.sleep(random.randint(1, 3))
    print("Here is your food.") 
    food = "Food"
    return food

async def main():
    tasks = []
    x = 1
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3],start=1):
            task = tg.create_task(student(x,sleep_time))
            tasks.append(task)
    results = [task.result() for task in tasks]
    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())
