#!/usr/bin/python3

# from threading import Thread
import threading
import time

'''函数方式'''
# start = time.time()

# def test():
    # for i in range(5):
        # print(threading.current_thread().name+'test',i)
        # time.sleep(2)

# thread = threading.Thread(target=test,name="TestThread",daemon=True)
# thread.start()
# thread.join(0.5)

# for i in range(5):
    # print(threading.current_thread().name+'main',i)
    # print(thread.name+' is alive',thread.isAlive())
    # time.sleep(1)

# end = time.time()

# print("duration:",end-start,'s')

'''类方法,重写run方法'''

class TestThread(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self,name=name)

    def run(self):
        for i in range(5):
            print(threading.current_thread().name+'test',i)
            time.sleep(1)

thread = TestThread(name="TestThread")
thread.start()

for i in range(5):
    print(threading.current_thread().name+' main',i)
    print(thread.name+' is alive',thread.isAlive())
    time.sleep(1)