'''目录遍历方法'''
import os
import glob



'''os.popen:调用shell命令,返回带\n的文件列表'''
# dl_popen = os.popen('dir /b').readlines()             #返回文件,文件夹列表
# for line in dl_popen:
    # print(line[:-1])                    #将后面的\n去掉

'''glob,更多匹配方式参见fnmatch模块; 返回文件路径列表'''
# dl_glob = glob.glob('*')
# dl_glob = glob.glob('*.csv')        #后缀是csv的
# dl_glob = glob.glob('f*')           #开头是'f'的
# dl_glob = glob.glob('?e*')         #第二个字母是e的, *匹配所有, ?匹配任意一个
# dl_glob = glob.glob('testfile')         #全名
# dl_glob = glob.glob('testfile\*')     #指定路径下的所有内容
# dl_glob = glob.glob('*\*.csv')     #从不同文件里匹配后缀csv的文件

# print(dl_glob)

# 分割与合并
# for file in glob.glob(r'C:\test1\*'):
    # head,tail = os.path.split(file)             #把路径和文件分开
    # print(head,tail,'==>',r"C:\test"+'\\'+tail)    
    



'''os.listdir:返回文件和文件夹名的列表; 它是鼻祖,os.walk, glob内部都是调用它'''
# dl_listdir = os.listdir()
# dl_listdir = os.listdir('.')
# dl_listdir = os.listdir(os.curdir)            #当前目录下的文件和文件夹列表
# dl_listdir = os.listdir(r'C:\Users\osun')             #传来的参数是路径

# print(dl_listdir)

# 分割与合并
# for file in os.listdir(r'C:\test1'):
    # print(r'C:\test1',file,"==>",os.path.join(r'C:\test1',file))        #os.path.join: 负责拼接

# os.walk: 是一个生成器函数; 返回元组:('路径','路径下的文件夹','路径下的文件')
# for (dirname, subshere, fileshere) in os.walk('.'):
    # print('['+dirname+']')
    # for fname in fileshere:
        # print(os.path.join(dirname,fname))
