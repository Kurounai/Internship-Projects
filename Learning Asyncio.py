import asyncio
import random


# Variables/lists
Menu = [1,2,3,4,5,6,7,8,9]

# Coroutines

async def customer(id):
    choice = random.choice(Menu)
    task = asyncio.create_task(waiter(choice))
    result = await task
    print(f"I have received my meal, id: {id}")

async def waiter(choice):
    task = asyncio.create_task(cook(choice))
    result = await task
    print(f"Here is your meal, a {result}")

async def cook(choice):
    print(f"The cook is now cooking a {choice}")
    await asyncio.sleep(choice)
    result = "Cooked Meal"
    return {result}

async def main():
   print("Taking all orders")
   task1 = asyncio.create_task(customer(1))
   task2 = asyncio.create_task(customer(2))
   task3 = asyncio.create_task(customer(3))
   result1 = await task1
   result2 = await task2
   result3 = await task3
   print("All orders are now complete.") 

asyncio.run(main())