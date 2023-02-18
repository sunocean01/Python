import queue
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import queue
import pandas as pd
import time
import threading


# conn = sqlite3.connect(r"C:\Sensirion\10_product\60_PM25\110_experiment\2022\20221110_DuplicatedLabel\db_Source\PM_Rework.db")
# c = conn.cursor()
# c.execute(r"INSERT INTO SEN4XDuplicateLabel values(null,'20221110','32342','403761010722J06926452501208881130S','601FB3DA182BD7EA','2','3','1')")
# conn.commit()

# q = queue.Queue()



# def writetodb():
    # while not self.q.empty():
    # gt = q.get()
    # print(gt)
    # c.execute(gt)
    # print("after execute")
    # conn.commit()
    # print("conmmit done")

# def cyc():
    # with ThreadPoolExecutor(max_workers=10) as pool:
        # for i in range(3):
            # q.put("insert into SEN4XDuplicateLabel values(null,'20221110','32342','403761010722J06926452501208881130S','601FB3DA182BD7EA','2','3','1')")
            # pool.submit(writetodb)
# time.sleep(15)
# c.close()
# conn.close()

# exit()

class Scanlabel:
    def __init__(self):
        # self.q = queue.Queue()
        self.conn = sqlite3.connect(r"C:\Sensirion\10_product\60_PM25\110_experiment\2022\20221110_DuplicatedLabel\db_Source\PM_Rework.db",check_same_thread=False)
        self.c = self.conn.cursor()
        self.df = pd.DataFrame(columns=["StartTime","position","DeviceId","box","tray","batchNr"])
    
    def writetodb(self,sql):
        # while not self.q.empty():
        # gt = self.q.get()
        print(sql)
        
        self.c.execute(sql)
        print("after execute")
        self.conn.commit()
        print("conmmit done")
        time.sleep(2)

    def cyc(self):
        sql = r"insert into SEN4XDuplicateLabel values(null,'20221110 13:00:00','32342','403761010722J06926452501208881130S','601FB3DA182BD7EA','2','3','1')"
        # self.writetodb(sql)
        
        self.thd = threading.Thread(target=self.writetodb,args=(sql,))
        self.thd.start()
        # with ThreadPoolExecutor(max_workers=10) as pool:
            # for i in range(3):
                # sql = r"insert into SEN4XDuplicateLabel values(null,'20221110','32342','403761010722J06926452501208881130S','601FB3DA182BD7EA','2','3','1')"
                # pool.submit(self.writetodb,args=(sql,))

    def __del__(self):
        # self.thd.join()
        self.c.close()
        self.conn.close()


if __name__ == "__main__":
    scanlabel = Scanlabel()
    scanlabel.cyc()