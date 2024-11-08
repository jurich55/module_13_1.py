import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for ball in range(1, 6):
        lift_time = 5 / power            # чем больше сила - тем меньше время
        await asyncio.sleep(lift_time)
        print(f'Силач {name} поднял {ball} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Циклоп', 5))
    task2 = asyncio.create_task(start_strongman('Геркулес', 8))
    task3 = asyncio.create_task(start_strongman('Геракл', 10))
             #   Запускаем одной строкой с помощью ".gather"
    await asyncio.gather(task1, task2, task3)


start = time.time()
asyncio.run(start_tournament())
finish = time.time()
print(f'время работы = {round(finish - start , 2)} секунд')