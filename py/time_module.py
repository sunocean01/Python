import time


'''time.altzone:返回格林威治西部的夏令时地区的偏移秒数。'''
# T = time.altzone
# ------------------
'''localtime:时间戳 --> 时间元组'''
# T = time.localtime()                      #返回此时此地的时间元组;
# T = time.localtime(1455508609.34375)      #返回时间戳对应的当地的时间元组;
'''asctime:时间元组 --> 可读时间"Tue Dec 11 18:07:14 2008"'''
# gettime = time.localtime()
# T = time.asctime(gettime)
# ---------------------------------
'''strftime(fmt[,tupletime]):时间元组 --> 可读时间，格式由fmt决定。'''
# T = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# T = time.strftime("%Y-%m-%d %H:%M:%S")                    #默认是此时此地时间
# -----------------------
'''ctime:时间戳 --> 可读时间"Mon Feb 15 11:56:49 2016"'''
# T = time.time()           #返回当前时间的时间戳,UTC时间
# T = time.ctime()                    #未给参数,相当于获取当时时间
# T = time.ctime(T)    #给定时间戳,将给的时间戳转换成当地可读形式
# ---------------------------
'''gmtime:时间戳 --> 格林威治天文时间下的时间元组'''
# T = time.gmtime(1455508609.34375)
# -----------------------------
'''mktime:时间元组 --> 时间戳'''
# T = time.mktime(T)
# --------------------------------------
'''sleep:推迟调用线程的运行，secs指秒数'''
# time.sleep(5)
# ------------------------
'''time.strptime(str,fmt='%a %b %d %H:%M:%S %Y'): 时间字符串 --> 时间元组'''
# T = time.strptime("30 Nov 00","%d %b %y")
# ----------------------------
'''time:返回此时的时间戳'''
# T = time.time()

print(T)



