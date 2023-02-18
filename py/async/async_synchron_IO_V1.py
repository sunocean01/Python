import asyncio
import time
import warnings
import functools
import random

warnings.simplefilter('ignore',ResourceWarning)

async def storage(data):
    with open('cro.txt','a') as fp:
        fp.write(data+'\n')

async def producer(queue,n):
    while True:
        item = input("Input:")
        print(f"producing {n}")
        await asyncio.sleep(random.random())
        # item = str(x)
        await queue.put(item)
        
        if item in ['q','Q']:
            break

async def consumer(queue,loop):
    while True:
        item = await queue.get()
        print(f"Consuming {item} ...")
        await asyncio.wait([asyncio.create_task(storage(str(item)))])
        queue.task_done()
        

async def main(n,loop):
    queue = asyncio.Queue(maxsize=10)
    consume = asyncio.ensure_future(consumer(queue,loop))
    await producer(queue,n)
    await queue.join()
    await asyncio.run(consume)
    consume.cancel()




# fp.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(10,loop))
# loop.close()

# s = time.time()

# asyncio.run(main())

# print(time.time()-s)

