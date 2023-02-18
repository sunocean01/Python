#!/usr/bin/python3

# from threading import Thread
import threading
import time
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()
# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    # with lock:
    for i in range(max):
        time.sleep(0.2)
        # print(threading.current_thread().name + ' ' + str(i))
        my_sum += i
    return my_sum

# action(50)



'''示例如何使用线程池'''
# 创建一个包含2条线程的线程池
# pool = ThreadPoolExecutor(max_workers=2)

# 分别向线程池提交两个任务, 50,100
# futurel = pool.submit(action,10)
# future2 = pool.submit(action,20)

# 判断任务是否结束
# print(futurel.done())


# time.sleep(3)

# print(future2.done())

# 查看任务返回的结果
# print(futurel.result())
# print(future2.result())

# pool.shutdown()

# print('-'*50)
# exit()
'''用add_done_callback()方法获取线程任务的返回值, 不会阻塞线程'''
with ThreadPoolExecutor(max_workers=2) as pool:
    futurel = pool.submit(action,10)
    future2 = pool.submit(action,20)
    
    def get_result(future):
        print(future.result())
        
    futurel.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    
    print("-"*50)

'''map()方法启动线程,并收集线程任务的返回值'''
# with ThreadPoolExecutor(max_workers=4) as pool:
    # results = pool.map(action,(5,10,50,15))
    # print('-'*50)
    # for r in results:
        # print(r)