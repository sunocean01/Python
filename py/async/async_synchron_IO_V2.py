import asyncio
import time
import warnings
import functools
import random

async def write(fp):
    fp.write(item+'\n')

# async def myinput():
    # x = input("Input:")
    # return x

async def product(queue,n):
    # for x in range(n):
    while True:
        x = input("Input:")
        print(f"producing {x}/{n}")
        # await asyncio.sleep(random.random())
        item = str(x)
        await queue.put(item)
        if x in ['q','Q']:
            break

async def consume(queue,fp):
    while True:
        item = await queue.get()
        print(f"consuming_{item}")
        await write(fp)
        # await asyncio.sleep(random.random())
        queue.task_done()

async def main(n,fp):
    queue = asyncio.Queue(maxsize=5)
    consumer = asyncio.ensure_future(consume(queue,fp))
    producer = asyncio.create_task(product(queue,n))
    
    await asyncio.wait([consumer,producer])
    # await queue.join()
    # consumer.cancel()

if __name__ == '__main__':

    fp = open("cro.txt","w",buffering=-1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(10,fp))
    fp.close()

