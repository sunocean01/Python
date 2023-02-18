import threading
import time
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import tkinter as tk
import asyncio
import queue

lock = threading.Lock()
fp = open(r".\os_subprocess\thtest.txt",'w',buffering=1)


def mywrite(num):
    lock.acquire()
    fp.write(num+'\n')
    time.sleep(5)
    lock.release()
    
while True:
    num = input('input:')
    
    thrd = threading.Thread(target=mywrite,args=(num,),name='th:'+num)
    thrd.start()
    
    print(thrd.getName())
    
    if num in ['q','Q']:
        break


thrd.join()
