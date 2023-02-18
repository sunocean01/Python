import urllib.request
import getopt
import sys

'''
getopt模块有两个函数，两个属性：
函数：
    getopt.getopt
    getopt.gnu_getopt
属性：
    getopt.error
    getopt.GetoptError

经常用到的是：getopt函数：
getopt.getopt(args, shortopts, longopts=[])
args:       指的是当前脚本接收的参数，它是一个列表，可以通过sys.argv获得
shortopts:  是短参数(必须)　　啥是短参数啊？　　类似于　这样：python test.py -h # 输出帮助信息
longopts:   是长参数(可选)　　啥是长参数啊？　　类似于　这样：python test.py -help # 输出帮助信息
'''

# arg = getopt.getopt(sys.argv[1:],'-h',['help'])     #其中shortopts是有,'-h'这个位置,也可以直接写字母'h'省略'-'
# print(arg)
'''或'''
# opts,args = getopt.getopt(sys.argv[1:],'-h',['help'])
# print(opts)
# print(args)

r''' 这个地方前面要加个r,否则会报错,不知道为什么:SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 196-197: truncated \UXXXXXXXX escape
#什么参数都不给,输出是包含两个列表的元组
C:\Users\osun\Desktop\Python\Function\library>python getopt_module.py
([], [])

C:\Users\osun\Desktop\Python\Function\library>python getopt_module.py Tomy 21 Grade1
([], ['Tomy', '21', 'Grade1'])

C:\Users\osun\Desktop\Python\Function\library>python getopt_module.py -h
([('-h', '')], [])

C:\Users\osun\Desktop\Python\Function\library>python getopt_module.py --help
([('--help', '')], [])
'''

# 假设我要接收一个参数+参数值的选项怎么办？
opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v',['help','filename=','version='])   #'-f:'或'filename=' 说明后面是需要输入参数的,长短可以混合使用
print(opts)
print(args)

r'''
C:\..\library>python getopt_module.py -h -f test1 --filename=file1 file2 file3
[('-h', ''), ('-f', 'test1'), ('--filename', 'file1')]
['file2', 'file3']
'''