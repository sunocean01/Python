'''pexpect是 Don Libes 的 Expect 语言的一个 Python 实现,是一个用来启动子程序，并使用正则表达式对程序输出做出特定响应，以此实现与其自动交互的 Python 模块。'''
import winpexpect

process = winpexpect.winspawn('dir')        #pexpect不能在windows下运行,winexpect才可以
print(process.winexpect(winpexpect.EOF))   # 打印index

# for i in winpexpect.__dict__:
    # print(i)

