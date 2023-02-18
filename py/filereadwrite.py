import csv

'''
此脚本主要用来介绍python3.x的基本函数&模块的用法
'''

'''open():打开文件,不管是读还是写,首先都要打开文件,一般和with语句配合使用,这样就不用f.close()关闭文件了'''
'''
mode参数选项:
t:文本模式 (默认)。

x:写模式，新建一个文件，如果该文件已存在则会报错。

b:二进制模式。如何使用此模式：Must have exactly one of create/read/write/append mode and at most one plus

+:打开一个文件进行更新(可读可写)。如何使用此模式：Must have exactly one of create/read/write/append mode and at most one plus

U: 通用换行模式（Python 3 不支持）。

r: 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。

rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。

r+: 打开一个文件用于读写。文件指针将会放在文件的开头。

rb+: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。

w: 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

wb: 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。

w+: 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

wb+:以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。

a: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

ab: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

a+: 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。

ab+: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

'''


'''
write:   将字符串写入文件
writelines: 将列表,元组等可迭代对象里的字符串写入文件,注意元素只能是字符串,不会做任何处理的写入,如换行,加空格等...
'''
fileph = r'.\filereadwrite\test.txt'
# string = 'Practise write to file!'
# with open(fileph,mode='w') as fp:      #with语句, + open函数,关键是mode参数,见open函数详解
    # fp.write(string)                        #将字符串写入文件;

lt = ['This','is','python','practice','!']
# lt = [1,2,4,6]     #数字的列表会报错
# with open(fileph,mode='w') as fp:
    # fp.writelines(lt)                       #Thisispythonpractice!: 将可迭代对象写入文件,它自己不会给添加任何内容(换行,空格..),当然字符串也是可迭代对象

'''
csv.writer(fp): 用打开的文件创建写入对象
writerow: ['abc','def'] ==> abc,def     在每个字符串之间加','
writerows: [['abc','def'],['ABC','DEF']] ==> abc,def        内部列表之间加'\n',在每个列表内部的字符串之间加',';
                                            ABC,DEF
'''

# data1 = ['abc','def']
# data2 = [['abc','def'],['ABC','DEF']]

# csvfile = r'.\filereadwrite\csvfiletest.csv'
# with open(csvfile,'a') as fp:
    # fpcsv = csv.writer(fp)
    # fpcsv.writerow(data1)               
    # fpcsv.writerows(data2)            

'''
内置读取文件方法:
    1. for循环方式读取;
    2. read([size]):按字节大小读取;
    3. readline([size]),一行一行的读取;
    4. readlines(): 读取并解析文件,['行1','行2'...'行n']
'''
csvfile2 = r'.\filereadwrite\sales_february_2019.csv'
# with open(csvfile2,'r') as fp:
    
    #迭代逐行读取
    # for value in fp:            
        # print(value)

    #fp.read([size]):如果不指定size,将文件全部读出为一个字符串;
    # bigstring = fp.read()
    # print(bigstring)
    
    #fp.readline([size]):一行一行的读取
    # line = fp.readline()
    # print(line)

    #fp.readlines():读取并解析文件         #效果同lt[:] = open(),将文件读到列表里去
    # filelist = fp.readlines()
    # print(filelist)
    # for line in filelist:
        # print(line,end='')

'''列表:将文件读到列表里去'''
# 方法一:
# L = []
# L[:] = open(csvfile2,'r')
# for i in L:
    # print(i,end='')

# 方法二:
# L = []
# L.append(open(csvfile2,'r'))
# for i in list(L[0]):
    # print(i,end='')
'''
csv模块读取文件方法:
    csv.reader(csvfile, dialect='excel', **fmtparams):  创建读对象
    
'''
# with open(csvfile2,'r') as fp:
    # csvfile = csv.reader(fp)        #csv.reader()返回的是对象,一行是一个列表,一个单元格是一个字符串
    # for i in csvfile:
        # print(i)