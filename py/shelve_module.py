"""本实例介绍shelve模块"""


import shelve




class Person:
    def __init__(self,name,age,pay=0,job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
        
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0+percent)

class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')
    def giveRaise(self,percent,bonus=0.1):
        Person.giveRaise(self,percent+bonus)
    
    
if __name__ == "__main__":
    '''信息输入'''
    # bob = Person('Bob Smith',42,30000,'software')
    # sue = Person('Sue Jones',45,40000,'hardware')
    # tom = Manager(name='Tom Doe',age = 50, pay=30000)
    
    '''信息查询'''
    # db = [bob,sue,tom]
    # for obj in db:
        # obj.giveRaise(.1)
    
    # for obj in db:
        # print(obj.lastName(),':',obj.pay)
    # with shelve.open(r".\testfile\db\employee.db") as fp:
        # fp['bob'] = bob
        # fp['sue'] = sue
        # fp['tom'] = tom
        # bob = fp['bob']
        # print(bob.name,bob.pay,bob.job,bob.age,bob.lastName())
        
        # for key in fp:                                  
            # print(key,':',fp[key].name,fp[key].pay) 
            # print(key,':',fp[key].__dict__)             #可以查询数据库里所有的条目及条目的所有属性
        
    
    '''shelve控制台界面查询'''
    filenames = ('name','age','job','pay')
    maxfield = max(len(f) for f in filenames)
    with shelve.open(r".\testfile\db\employee.db") as fp:
        while True:
            key = input('\nkey?=>')     #键或者空行退出
            if not key: 
                break
            try:
                record = fp[key]        #依据键获取记录
            except:
                print('not such key {}'.format(key))
            else:
                for field in filenames:
                    print(field.ljust(maxfield),"=>",getattr(record,field))