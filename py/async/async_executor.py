import asyncio
import time
# import warnings
# import functools
# import random
# from concurrent.futures import ThreadPoolExecutor

async def inpt(queue):
    while True:
        item = input("Input:")
        
        if item in ['q','Q']:
            await queue.put(item)
            break
        else:
            await queue.put(item)
    return 0

async def writedown(queue,fp):
    print("writedown run")
    i = 0
    while True:
        print(f"writedown:{i}")
        it = await queue.get()
        i = i+1
        if it not in ['q','Q']:
            fp.write(it)
            fp.flush()
            print(f"fp:{i}")
        else:
            break
    return 0

async def main():
    fp = open('corotext.txt','w',buffering=1)
    queue = asyncio.Queue(maxsize=4)
    tasks = [asyncio.create_task(inpt(queue),name='inpt'),
             asyncio.create_task(writedown(queue,fp),name='writedown')]
             
    done,pending = await asyncio.wait(tasks,timeout=None,return_when='ALL_COMPLETED')
    # print(done)
    for tk in done:
        print(type(tk))
    print("*"*60)
    print(pending)
    fp.close()
if __name__ == '__main__':

    asyncio.run(main())
