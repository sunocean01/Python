import threading
import queue
import time


class ThreadWrite():
    def __init__(self):
        self.q = queue.Queue()
        self.fp = open('test.txt','w',buffering=1)

    def write(self):
        time.sleep(3)
        self.fp.write(self.q.get())

    def iteration(self):
        while True:
            nm = input("input:")
            
            if nm=='q':
                break
            else:
                self.q.put(nm+'\n')
                self.thr = threading.Thread(target=self.write)
                self.thr.start()
    
    def __delete__(self):
        self.thr.join()
        self.fp.close()

if __name__ == '__main__':
    txt = ThreadWrite()
    txt.iteration()