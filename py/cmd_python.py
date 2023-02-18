import os
import subprocess

''' 第一种方式: os.system('命令'), 没有返回值;'''
# running = os.system(r'python C:\Users\osun\Desktop\Python\Function\testfile\cmd_python_model.py')
# running = os.system(r'dir')

''' 第二种方式: os.popen('命令'), 有返回值'''
# result = os.popen(r'python C:\Users\osun\Desktop\Python\Function\testfile\cmd_python_model.py')
# result = os.popen(r'dir')
# res = result.read()
# print(res)

''' 第三种方式: os.exec***: 执行一个新的程序，然后用新的程序替换当前子进程的进程空间'''


# interpreter = r"C:\work\virtenvs\3p5_64bit_SensiPython_3p0\Scripts\python.exe"
# script = r"C:\Users\osun\Desktop\Python\Function\testfile\cmd_python_exec_model.py"

# os.execl(interpreter,"python",script,'exec_example test') # os.execl*系列表示的是接受的参数是一个个独立的参数传进去了

# os.execv(interpreter,["python",script,'python test'])   # os.execv* 系列表示接受的是一个list或者是一个tuple表示的参数表

# os.execlp("python","python",script,"python test")

# os.execle("python","python",script,"python test",os.environ)


''' 第四中方式: subprocess模块,见subprocess_module.py 介绍'''
'''
run():等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
call():其功能类似于os.system(cmd)
check_call():执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(…, check=True)。
check_output():执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常。
getoutput(cmd):接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
etstatusoutput(cmd):执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)，其功能类似于commands.getstatusoutput()。
Popen(): run方法底层用的是Popen()
poll():检查进程的状态

'''

# p = subprocess.run(r'python C:\Users\osun\Desktop\Python\Function\testfile\cmd_python_model.py',shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# res = p.stdout
# print(res)
# print(str(res,'utf8'))

