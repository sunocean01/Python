import multiprocessing
import time

'''父进程和子进程之间通讯需要导入'''
from multiprocessing import Process, Pipe


# start = time.time()
def worker1(interval):
    n = 3
    while n>0:
        print('worker1 {}'.format(time.ctime()))
        time.sleep(interval)
        n -= 1

def worker2(interval):
    n = 5
    while n>0:
        print('worker2: {}'.format(time.ctime()))
        time.sleep(interval)
        n -= 1

def worker3(interval):
    n = 7
    while n>0:
        print('worker3 {}'.format(time.ctime()))
        time.sleep(interval)
        n -= 1

'''父进程和子进程之间通讯需要导入'''
def sender(pipe):
    '''在匿名管道上向父进程发送对象'''
    pipe.send(['spam']+[42,'eggs'])
    pipe.close()

def talker(pipe):
    '''通过管道发送和接收对象'''
    pipe.send(dict(name='Bob',spam=42))
    reply = pipe.recv()
    print('talker got:',reply)



if __name__ == "__main__":
    '''多进程示例:'''
    # p1 = multiprocessing.Process(target=worker1,args=(2,))
    # p2 = multiprocessing.Process(target=worker2,args=(1,))
    # p3 = multiprocessing.Process(target=worker3,args=(0.5,))
    # start = time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    
    # p1.join()
    # p2.join()
    # p3.join()
    # end = time.time()
    # print("pid:",p1.pid,p2.pid,p3.pid)
    # print("name:",p1.name,p2.name,p3.name)
    # print("alive:",p1.is_alive(),p2.is_alive(),p3.is_alive())
    # print(end-start)
    
    
    # '''父进程和子进程间发送和接收数据'''
    # (parentEnd, childEnd) = Pipe()
    # Process(target=sender, args=(childEnd,)).start()
    # print('parent got:',parentEnd.recv())
    # parentEnd.close()
    
    # (parentEnd,childEnd) = Pipe()
    # child = Process(target=talker, args=(childEnd,))
    # child.start()
    # print('parent got:',parentEnd.recv())
    # parentEnd.send({x*2 for x in 'spam'})
    # child.join()
    # print('parent exit')
    