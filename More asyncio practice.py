import asyncio
import random
from Car_Module import Car

# Vars/Lists
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")
car_3 = Car("Bugatti","Chiron",2009,"White")
car_4 = Car("Ferarri","Dodge Viper",2024,"Black")
cars = [car_1,car_2,car_3,car_4]


# coroutines
async def customer(choice,id,x):
    if x == 1:
        print(f"Hello, I would like to buy a {choice.make}")
        print(f"Could you please tell me some information about the car?")
        task1 = asyncio.create_task(salesman(choice,id,1))
        await task1
    if x == 2:
        print(f"How much would the {choice.make} cost?")
        task2 = asyncio.create_task(salesman(choice,id,2))
        cost = await task2
        print(f"Customer {id} has bought a {choice.make} for {cost}")
    x = 0

async def salesman(choice,id,x):
    if x == 1:
        print(f"Hello, Customer {id}, I will gladly inform you about the car.")
        print(f"That {choice.make} is a {choice.year}, {choice.make} {choice.model} with a premium {choice.color} paint job.")
        task1 = asyncio.create_task(customer(choice,id,2))
        await task1
    if x == 2:
        print("Please wait while I contact the bank to find out it's price.")
        task2 = asyncio.create_task(bank(choice))
        cost = await task2
        await asyncio.sleep(id*2)
        print(f"The cost of that {choice.make} is {cost}")
        return cost
    x = 0

async def bank(choice):
    if choice.model == "Corvette":
        cost = 100000
    if choice.model == "Mustang":
        cost = 50000
    if choice.model == "Chiron":
        cost = 1000000
    if choice.model == "Dodge Viper":
        cost = 75000
    return cost
async def main():
    print("Starting car deals")
    choice = random.choice(cars)
    deal1 = asyncio.create_task(customer(choice,1,1))
    choice = random.choice(cars)
    deal2 = asyncio.create_task(customer(choice,2,1))
    choice = random.choice(cars)
    deal3 = asyncio.create_task(customer(choice,3,1))
    finalize1 = await deal1
    finalize2 = await deal2
    finalize3 = await deal3
    print("All deals have now been completed.")
asyncio.run(main())