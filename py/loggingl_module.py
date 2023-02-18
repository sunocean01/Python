import logging

# logging.basicConfig():设置日志级别,默认debug是不打印的
'''
filename	指定使用指定的文件名而不是 StreamHandler 创建 FileHandler。
filemode	如果指定 filename，则以此模式打开文件(‘r’、‘w’、‘a’)。默认为“a”。
format	为处理程序使用指定的格式字符串。
datefmt	使用 time.strftime() 所接受的指定日期/时间格式。
style	如果指定了格式，则对格式字符串使用此样式。’%’ 用于 printf 样式、’{’ 用于 str.format()、’$’ 用于 string。默认为“%”。
level	将根记录器级别设置为指定的级别。默认生成的 root logger 的 level 是 logging.WARNING，低于该级别的就不输出了。级别排序：CRITICAL > ERROR > WARNING > INFO > DEBUG。（如果需要显示所有级别的内容，可将 level=logging.NOTSET）
stream	使用指定的流初始化 StreamHandler。注意，此参数与 filename 不兼容——如果两者都存在，则会抛出 ValueError。
handlers	如果指定，这应该是已经创建的处理程序的迭代，以便添加到根日志程序中。任何没有格式化程序集的处理程序都将被分配给在此函数中创建的默认格式化程序。注意，此参数与 filename 或 stream 不兼容——如果两者都存在，则会抛出 ValueError。
原文链接：https://blog.csdn.net/colinlee19860724/article/details/90965100
format格式参数:
    %(levelno)s	打印日志级别的数值
    %(levelname)s	打印日志级别名称
    %(pathname)s	打印当前执行程序的路径
    %(filename)s	打印当前执行程序名称
    %(funcName)s	打印日志的当前函数
    %(lineno)d	打印日志的当前行号
    %(asctime)s	打印日志的时间
    %(thread)d	打印线程id
    %(threadName)s	打印线程名称
    %(process)d	打印进程ID
    %(message)s	打印日志信息
'''
# logging.basicConfig(level=logging.ERROR,format="%(levelno)s-(asctime)s-%(levelname)s-%(message)s") 


# 1. logger:提供应用程序代码直接使用的接口
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


# 2. Handler: 对信息处理,默认处理warning以上级别
fh = logging.FileHandler(r".\testfile\log.log")  #将信息存入文件
ch = logging.StreamHandler()        #为了同时输出到文件和屏幕,所以这两个都是配置

# 2-1. Fommatter:对信息进行格式化, 下面单个格式是固定的,只要选择即可
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(file_formatter)

# 2-2. 设置处理信息的级别
fh.setLevel(logging.WARN)

ch.setFormatter(file_formatter)
ch.setLevel(logging.WARN)

# 2-3. 创建过滤,并添加到handler,也可以添加奥logger
filter_name = logging.Filter(__name__)
# fh.addFilter(filter_name)
logger.addFilter(filter_name)

# 3. 将handler添加到logger
logger.addHandler(fh)
logger.addHandler(ch)   

# 将信息打印到控制台
'''
debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上
info : 打印info,warning,error,critical级别的日志,确认一切按预期运行
warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作
error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能
critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
原文链接：https://blog.csdn.net/weixin_39864453/article/details/114911510
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
'''
logger.debug("孙悟空")
logger.info("猪八戒")
logger.warning("沙僧")
logger.error("唐僧")
logger.critical("白龙马")

