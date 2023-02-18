
from functools import wraps

'''
本例主要用来介绍函数装饰器:
装饰器理解:不对已有函数做任何修改的情况下,对函数实现的功能稍做修改,如它的名称"装饰"
'''

# 首先需要理解函数特性,及闭包函数
# 1. 函数可以作为变量传递

def add(x):
    print('add function:',x+1)
    return x+1

# a = add             #不带(),只是作为变量进行传递;
# b = add(2)           #带(),add函数会被执行
# a(2)                 #实际 a() 等于 add()
# b                   #b是接收add(2)的返回值的

# 2. 函数作为参数传递:
def excute(f):
    print('excute function:',f(3))

# excute(add)         #add作为参数传递给另一个函数


# 3. 函数作为返回值
def get_add():
    return add

# a = get_add()       #a接收get_add()的返回值
# a(3)


# 4. 函数嵌套及跨域访问
def outer():
    x = 1
    def inner():
        print(x)
    inner()
# outer()

'''总结:
    1. 要把函数进行传递返回时:     只用函数名,如: add
    2. 要执行函数时:               函数名+(),如:  add()
'''


# 闭包函数:

def func():
    return "函数func"

def outer(x):
    def inner():        #函数嵌套
        return x        #跨域访问,引用了外部变量x,注意x和x()的区别
    return inner        #函数作为返回值

closure = outer(func) #函数作为变量附给closure

# print(func())
# print(closure())        #执行闭包

'''
closure实际上是outer(func)，func作为参数传进outer，outer的子函数inner对func返回的结果进行了一番装饰，返回了一个装饰后的结果，最后outer返回inner，可以说inner就是装饰后的func，这就是一个函数被装饰的过程，重点在于执行 outer(func) 这个步骤。
'''

# 装饰器语法糖@

def outer(x):
    def inner():                             #函数嵌套
        return x()+' After decorated'        #对传入的函数运行结果做修改
    return inner                             #函数作为返回值

@outer
def func():
    return "函数func"

# print(func())

'''
就是拿来把被装饰的函数作为参数传递到装饰器函数里面加工的，最后执行被装饰函数的时候，就相当于执行了一个加工后的函数。
'''
# --------------------------------------------------------以上是装饰器基本概念-------------------------------------------------
'''wraps():'''
def outer(x):
    @wraps(x)
    def inner():                             #函数嵌套
        return x()+' After decorated'        #对传入的函数运行结果做修改
    return inner                             #函数作为返回值

@outer
def func():
    return "函数func"

# print(func.__name__)   #inner: func()函数的函数名不是'func'吗? 怎么变成inner了呢? 因为适用装饰, 可以用@wraps(x)对装饰器进行装饰.

'''
带参数的装饰:在函数中嵌入装饰器
'''

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
 
@logit()
def myfunc1():
    pass
 
# myfunc1()

'''
@property
'''
