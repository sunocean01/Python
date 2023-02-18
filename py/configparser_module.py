'''configparser的作用是读取ini文件'''

import configparser
import os

'''https://www.cnblogs.com/cangqinglang/p/13657427.html'''

IniFile = r'.\testfile\FairfieldCalibration.ini'
configPath = r'.\testfile\FairfieldCalibration.ini'

cp = configparser.ConfigParser()        #实例化

cp.read(IniFile)    #读取ini配置文件

'''sections():读取文件中所有的section'''
# secs = cp.sections()
# print(secs)

'''options('section'):获取指定section中的键,返回列表'''
# options = cp.options('Plc')
# print(options)

'''items():读取指定section中的键值对,返回形式:元组嵌套在列表中'''
# items = cp.items('Plc')
# print(items)

'''get('section','key'): 读取指定section下面指定的key的值'''
# Val = cp.get('Plc','port')
# print(Val)


exit()
class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self, param):
        value = self.cf.get("Plc", param)
        return value

    def get_db(self, param):
        value = self.cf.get("Tsi", param)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    LocalIp = test.get_http('Port')
    print(LocalIp)


























