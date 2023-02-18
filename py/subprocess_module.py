import subprocess       #内置模块

'''subprocess.run(): 在windows下执行一条cmd命令!!!
args：                   表示要执行的命令。必须是一个字符串，字符串参数列表。
stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。subprocess.PIPE 表示为子进程创建新的管道。subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。另外，stderr 可以合并到 stdout 里一起输出。
timeout：                设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。
check：                  如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。
encoding:                python3.6 以上可用,如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。
shell：                  如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
'''

'''运行条cmd命令'''
# subprocess.run(args="python",shell=True)      #运行python
# subprocess.run(args="dir",shell=True)      #运行dir

# subprocess.run(args="pip list",shell=True)    #这两种方式都可用
# subprocess.run(args=["pip","list"],shell=True)    

# subprocess.run(args="python function_test.py",shell=True)   #function_test.py 与此脚本在同一目录下是可用的,否则要用列表,如下一条
# subprocess.run(["python",r".\testfile\function_test.py"],shell=True)

# subprocess.run(args="pip list",shell=True)


'''通过cmd打开一个软件'''
# subprocess.run([r"C:\Windows\System32\notepad.exe"],shell=True)

'''通过命令行运行脚本,及将运行后的结果存到文件'''
# with open(r".\testfile\subprocessruntest.csv",'w') as fp:
    # subprocess.run(["python",r".\testfile\function_test.py"],shell=True,timeout=2,stdout=fp)


'''subprocess.run()的返回值'''
# p = subprocess.run("echo hello dj", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print("获取返回对象:{}".format(p))
# print("获取执行命令:{}".format(p))
# print("获取返回码:{}".format(p.returncode))
# print("获取返回数据:{}".format(p.stdout))

# res = p.stdout.decode()   #stdout返回的是二进制字节,decode()转换成字符串
# print(res)

'''subprocess.call():已经被subprocess.run()方法取代'''


'''subprocess.Popen():在windows下执行一条cmd命令!!!

subprocess.run()是通过subprocess.Popen()来实现的
subprocess.Popen()可以异步执行
'''
'''
○ args：         要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
○ bufsize：      指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
○ stdin, stdout, stderr： 分别表示程序标准输入、输出、错误句柄。
○ preexe：       用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
○ close_fds：    如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
○ shell：        该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，则建议将args参数作为一个字符串传递而不要作为一个序列传递。
○ cwd：          如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
○ env：          用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。如果env!=None，它的值必须是一个映射对象。
○ universal_newlines： 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，否则他们将会被作为二进制流被打开。
startupinfo和creationflags： 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如主窗口的外观
'''

'''在windows下执行cmd命令：echo chinablue
subprocess.Popen()方法是一个异步方法，执行后会返回一个Popen对象!!!
'''
p = subprocess.Popen("echo this is test", shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# print("获取返回对象: {}".format(p))
# print("获取pid: {}".format(p.pid))
# print("获取返回数据: {}".format(p.stdout.read()))
# p.wait()
# print("获取执行状态: {}".format(p.poll()))

'''

2) 获取子进程的标准输出(stdout)和标准错误(stderr)
    方式1：通过p.stdout和p.stderr获取，如上例所示
    方式2：通过p.communicate()获取，它返回一个元祖，元祖的第1个元素为stdout内容，元祖的第2个元素为stderr内容
'''
# print("获取返回数据{}".format(p.communicate()))

# for i in p.communicate():
    # print(i)

# --------------------------------------------------------------

# obj = subprocess.Popen(["python","function_test.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8')

'''对子进程的交互输入:'''
'''方法一:obj.stdin.write 方法'''
# obj.stdin.write("python test \n")
# obj.stdin.write(print(2))
# out= obj.communicate()[0]
# print(out)
# exit()
'''方法二:使用communicate()里面的input参数'''
# out= obj.communicate(input='this is python test')[0]
# print(out)
# ----------------------------------------------------------------------

# obj = subprocess.Popen(["python"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8')
# obj.stdin.write("print('this is python test') \n")
# obj.stdin.write("print('2nd print out')")
# out = obj.communicate()[0]
# print(out)
# -----------------------------------------
'''stdout可以使用read(),readline(),readlines()等方法'''
# obj = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf8')
# out = obj.stdout.readlines()   #这两个都是输出
# out = obj.communicate()[0]
# print(out)
# ---------------------------------------------------------

# obj = subprocess.Popen(r"python",shell=True,stdin=print("a-b".split('-')),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# out = obj.communicate()[0]
# print(out)


# --------------------------------------------------------
''' 3) p.poll():用于检查子进程（命令）是否已经执行结束，没结束返回None，结束后返回状态码。'''
'''
如果执行完subprocess.Popen()方法后，立即获取命令的执行状态, 则返回结果为None，因为此时子进程扔在运行中
如果我们需要等待子进程运行完毕后，再去获取命令的执行状态。那么我们可以使用p.wait()方法，这相当于将默认的异步操作改为同步操作
'''
# print(p.poll())
# p.wait()
# print(p.poll())

exit()

# ret = subprocess.run("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
# ret.stdin = "print('haha')"     # 错误的用法
# print(ret)