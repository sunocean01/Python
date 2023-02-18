import threading
import time
import sensirion_fastedf as sf
import glob
import tqdm
import os
import pandas as pd
import queue
from concurrent.futures import ThreadPoolExecutor

'''多线程的使用有两种方式: 1. 利用回调函数; 2. 重写Thread类方法;'''

'''第一种: 利用回调函数'''
'''threading.Thread(): 创建线程'''
'''
target: 要传入的回调函数,注意只是函数名,是不带括号;
args: 回调函数需要传入的参数;
name: 线程的名称, 默认格式:Thread-N,N是数字
daemon: 默认False, 主线程是否要等待子线程结束后再结束; 如果主线程结束,子线程也会跟着结束
'''

'''Thread的方法'''
'''
start(): 启动线程;
join(): join()线程调用该函数之后，将在执行完该线程之后继续主线程，否则主线程会与启动的子线程同步执行
isAlive(): 线程是否存活
getName(), 获取线程名称;
setName(), 设置线程名称;

Lock():是线程安全的方法,如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。既保证每次只有一个线程对某个数据进行修改，在实际输入输出、连接数据库插入数据时个人曾经遇到过格式混乱、内容错误的问题，想来也是由于多个线程同时执行某个操作导致的。
其实单个线程多次调用I/O等操作时不怕，就怕多个线程同时进行调用，则会混乱，若是插入数据库时存在这样的混乱则数据库很难看，可能会导致数据没有参考价值。
'''


start = time.time()
lock = threading.Lock() #创建一个互斥锁


# def print_time(num):
    # # lock.acquire()
    # for i in range(num):
        # time.sleep(0.5)
        # print(threading.current_thread().name,time.ctime())
    # # lock.release()

# lock的另外一种写法:
# def print_time(num):
    # with lock:
        # for i in range(num):
            # time.sleep(0.2)
            # print(threading.current_thread().name,time.ctime())

# thread_a = threading.Thread(target=print_time,args=(5,),name='a')
# thread_b = threading.Thread(target=print_time,args=(10,),name='b')

# thread_a.start()
# thread_b.start()

# thread_a.join()
# thread_b.join()

# print("Main fishnied")



'''queue.Queue(maxsize=0): 是线程安全的类;在多个线程同时访问时不会出现问题，如果 maxsize 设置为小于或等于零，则队列的长度没有限制。'''
'''
qsize()，返回队列大小
empty() 如果队列为空，返回True,反之False
get() 获取对列的值
put() 向队列中添加数值。
Queue.task_done()在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join()实际上意味着等到队列为空，再执行别的操作
'''
num = queue.Queue()

for i in range(10):
    num.put(i)

lt = []
def fetch(num):
    # with lock:
    while not num.empty():
        lt.append(num.get())
        # print(num.get())


if __name__ == "__main__":
    th1 = threading.Thread(target=fetch,args=(num,))
    th2 = threading.Thread(target=fetch,args=(num,))
    th3 = threading.Thread(target=fetch,args=(num,))

    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()

    end = time.time()
    print(lt)
    print("Duration:",end-start,'s')



























