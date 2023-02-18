import datetime
import time
import pytz


# 今天 today = datetime.date.today()
# 昨天 yesterday = today - datetime.timedelta(days=1)
# 上个月 last_month = today.month - 1 if today.month - 1 else 12
# 当前时间戳 time_stamp = time.time()
# 时间戳转datetime datetime.datetime.fromtimestamp(time_stamp)
# datetime转时间戳 int(time.mktime(today.timetuple()))
# datetime字符串格式化 today_str = today.strftime("%Y-%m-%d")
# 字符串转datetime today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
# 补时差 today + datetime.timedelta(hours=8)
'''
datetime模块定义了下面这几个类:下面这些类对象是不可变的
datetime.date:表示日期的类.常用属性: year,month,day;
datetime.time:表示时间的类.常用属性有hour,minute,second,microsecond;
datetime.datetime:表示日期时间;
datetime.timedelta:表示时间间隔,即两个时间点之间的长度;
datetime.tiznfo:与时区相关的信息;
'''

'''date类:
date类原形: class datetime.date(year,month,day)
year: 范围[MINYEAR,MAXYEAR],即[1,9999];
month: 范围[1,12],(月份是从1开始,不是0);
day:最大值根据给定的year,month参数决定;
'''

'''
date类定义了如下一些常用的方法与属性:
'''
'''max/min:date对象能表示的最大,最小日期'''
# D = datetime.date.max
# D = datetime.date.min
# ----------------------------
'''resolution:date对象表示日期的最小单位'''
# D = datetime.date.resolution
# -------------------
'''today():返回一个表示当前本地日期的date对象'''
# D = datetime.date.today()
# ------------------
'''fromtimestamp(timestamp):时间戳 --> date对象'''
# D = datetime.date.fromtimestamp(time.time())
# -----------------------------------------------------------------------------------------
'''date类提供了如下一些方法和属性'''
'''date.year,date.month,date.day:分别获取date的年,月,日'''
# D = datetime.date.today()
# D = datetime.date(2020,12,10)       #注意:月和日是个位数时前面不能加0,如: 5月是:5,不能写成05;
# D = D.year
# D = D.month
# D = D.day
'''date.replace(year,month,day):生成一个新的日期对象,用参数指定的年,月,日代替原有对象中的属性.(原有对象仍保持不变)'''
# today = datetime.date.today()
# Day = today.day
# D = today.replace(day=Day+1)
'''date.timetuple:返回日期对应的time.struct_time(时间元组)对象'''
# today = datetime.date.today()
# D = today.timetuple()
'''date.weekday():返回weekday,如果是星期一,返回0,星期二,返回1,以此类推;'''
# today = datetime.date.today()
# D = today.weekday()
'''date.isoweekday():返回weekday,如果是星期一,返回1,星期二,返回2,以此类推;'''
# today = datetime.date.today()
# D = today.isoweekday()
'''date.isocalendar():返回格式(year,month,day)的元组;'''
# today = datetime.date.today()
# D = today.isocalendar()
'''date.isoformat():返回格式如'YYYY-MM-DD'的字符串'''
# today = datetime.date.today()
# D = today.isoformat()
'''date.strftime():自定义格式化字符串'''
# today = datetime.date.today()
# D = today.strftime('%Y%m%d')


'''date重载了简单的运算符:'''
'''date2 = date1 + timedelta'''
# today = datetime.date.today()
# D = today + datetime.date.resolution
'''date2 = date1 - timedelta'''
# today = datetime.date.today()
# D = today - datetime.date.resolution
'''timedelta = date1 - date2'''

'''date1 < date2'''
# today = datetime.date.today()
# D = today < datetime.date.max

# -----------------------------------------------------------------------------------
'''time 类:表示时间(由时,分,秒,微秒组成),原型如下:'''
'''
class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
hour: 范围[0,24]
minute:范围[0,60]
microsecond:范围[0,1000000]
tzinfo:表示时区信息
'''
'''time类属性:'''
'''min/max:time能表示的最小和最大时间'''
# D = datetime.time.min
# D = datetime.time.max
'''resolution:时间的最小单位,这里是1微秒'''
# D = datetime.time.resolution
# ---------------------------------------
'''time类提供的方法和属性'''
'''hour\minute\second\microsecond: 时分秒,微秒
tzinfo: 时区信息
'''
# D = datetime.time(7,34,50)
# D = D.hour
# D = D.minute
# D = D.second
# D = D.tzinfo
'''isoformat: 返回型如"HH:MM:SS"格式的字符串表示'''
# D = datetime.time(7,34,50)
# D = D.isoformat()
'''replace[hour[,minute[,second[,microsecond]]]]:创建一个新的时间对象,用指定的时,分,秒,微秒代替原由对象中的属性(原有对象保持不变)'''
# D = datetime.time(7,34,50)
# D = D.replace(minute=10)
'''strftime:返回自定义格式化字符串'''
# D = datetime.time(7,34,50)
# D = D.strftime('%I:%M:%S %p')       #参见日期格式代码

'''注:time类的对象只能进行比较,无法进行加减操作'''
# ------------------------------------------------------------

'''datetime类'''
'''datetime是date与time的结合体,包括date与time的所有信息.原型如下:
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
各个参数与date,time的构造函数中一样,要注意参数的范围
'''

'''datetime类定义的类属性与方法'''
'''min/max:datetime所能表示的最小值和最大值'''
# D = datetime.datetime.min
# D = datetime.datetime.max
'''resolution:datetime最小单位'''
# D = datetime.datetime.resolution        #通过print打印结果:'0:00:00.000001'; shell中直接运行datetime.datetime.resolution:datetime.timedelta(0, 0, 1)

'''today():返回一个表示当前本地时间的datetime格式日期'''
# D = datetime.datetime.today()
'''now([tz]):返回一个当前本地时间的datetime对象,如果提供了参数tz，则获取tz参数所指时区的本地时间'''
# tz = pytz.timezone('Asia/Shanghai')     #获取时区信息
# tz = pytz.timezone('Europe/Stockholm')     #获取时区信息
# D = datetime.datetime.now(tz=tz)

'''datetime.utcnow()：返回一个当前utc时间的datetime对象,0时区的时间'''
# D = datetime.datetime.utcnow()

'''fromtimestamp(timestamp[.tz]): 时间戳 --> datetime对象,默认给转换成你当地的时区了'''
# D = datetime.datetime.fromtimestamp(time.time())

'''utcfromtimestamp(timestamp): 时间戳 --> utc datetime对象'''
# D = datetime.datetime.utcfromtimestamp(time.time())

'''combine(date,time):根据date,time创建一个datetime对象'''
# D = datetime.datetime.combine(datetime.date(2020,12,4),datetime.time(8,36,40))

'''strptime(date_string,format): 格式字符串 --> datetime对象, date和time类没有该属性'''
# D = datetime.datetime.strptime('20-12-05','%y-%m-%d')       #后面的这个格式是和前面字符串对应的,意思就是给一个字符串同时告诉python该字符串表示的意思;

# ---------------------------------------------------------------

'''datetime提供的方法和属性'''
'''year,month,day,hour,minute,second,microsecond:年月日,时分秒,微秒'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = D.year
# D = D.month
# D = D.day
# D = D.hour
# D = D.minute
# D = D.second
# D = D.microsecond
'''date()/time():获取date/time对象'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = D.date()
# D = D.time()
'''replace([year[,month[,day[,hour[,minute[,second[,microsecond]]]]]]]):同date/time的replace方法'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = D.replace(hour=10)
# ----------------------
'''timetuple(): 返回时间元组'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = datetime.datetime.timetuple(D)
# -----------------
'''utctimetuple:返回utc时间元组'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = datetime.datetime.utctimetuple(D)
# ---------------------------------
'''weekday:返回weekday,如果是星期一,返回0,星期二,返回1,以此类推;'''
# D = datetime.datetime(2020,12,5,8,44,30,3000)
# D = D.weekday()
# --------------------
'''isocalendar:返回格式(year,month,day)的元组'''
# D = datetime.datetime.fromtimestamp(time.time())
# D = D.isocalendar()
# ------------------------------
'''isoformat:返回格式如'2020-12-13T16:51:58.688978'的字符串'''
# D = datetime.datetime.fromtimestamp(time.time())
# D = D.isoformat()
# ------------------------------
'''ctime():返回一个日期时间的C格式字符串,等效于time.ctime(time.mktime(dt.timetuple()))'''
# D = datetime.datetime.fromtimestamp(time.time())
# D = D.ctime()
# ----------------------------
'''strftime():自定义格式化字符串'''
# D = datetime.datetime.today()
# D = D.strftime('%U')
# --------------------

'''datetime.timedelta类:代表两个时间之间的时间差,两个date或datetime对象相减时可以返回一个timedelta对象'''

'''
class datetime.timedelta(days=0,seconds=0,microsceconds=0,milliseconds=0,minutes=0,hours=0,weeks=0)
所有参数可选,且默认都是0,参数的值可以是整数,浮点数,正数或者负数.内部只存储days,seconds,microseconds,其他参数的值会自动按如下规则转换:
1 millisecond(毫秒)  --> 1000microseconds(微秒)
1 minute --> 60 seconds
1 hour --> 3600 seconds
1 week --> 7 days
三个参数的取值范围:
0 < microseconds < 1000000
0 < seconds < 3600*24(一天的秒数)
-999999999 < days < 999999999
'''
# --------------------------------------
'''timedelta类属性'''
'''min:时间间隔对象的最小值,即timedelta(-999999999)'''
# D = datetime.timedelta.min
# ----------------------------
'''max:时间间隔对象的最大值,即timedelta(days=999999999,hours=23,minutes=59,seconds=59,microseconds=999999)'''
# D = datetime.timedelta.max
# --------------------------------
'''resolution:时间间隔的最小单位,即timedelta(microseconds=1)'''
# D = datetime.timedelta.resolution

'''timedelta方法'''
'''timedelta.total_seconds():计算时间间隔的总秒数'''
# D = datetime.timedelta.resolution.total_seconds()

'''计算两个时间的差,默认单位是秒'''
'''
timedelta.total_seconds(): 两个时间点之间的秒数
timedelta.days:     两个时间点之间的天数
'''
# time1 =  datetime.datetime.strptime('2020-12-01 08:01:47.657972+08:00', "%Y-%m-%d %H:%M:%S.%f+08:00")
# time2 =  datetime.datetime.strptime('2020-12-08 08:14:57.657972+08:00', "%Y-%m-%d %H:%M:%S.%f+08:00")
# span = time2-time1

# D = span.total_seconds()        #返回的结果单位是秒
# D = span.days                   #返回两个时间点之间的天数差

'''当前时间+固定时间差: 未来的时间点'''
cur = datetime.datetime.now()
# targetT = cur + span
targetT = cur+datetime.timedelta(2)     #timedelta(2),这个2指是2天;
print(targetT)
exit()


print(D)

'''datetiem.date类,datetime.time类,datetime.timedelta类, 都提供了都提供了strftime()方法'''

'''
%a 是星期的简写; 如 星期三:Web;
%A 是星期的全写; 如 星期四: Wednesday;
%b 月份的简写; 如 4月份: Apr;
%B 月份的全写; 如 4月份:April;
%c 日期时间的字符串表示; 如 04/07/10 10:43:39;
%d 日在这个月中的天数(这个月的第几天);
%f 微秒(范围[0,999999])
%H 小时(24小时制,[0,23])
%I 小时(12小时制,[0,23])
%j 日在年中的天数[001,366](当年的第几天)
%m 月份[01,12]
%M 分钟[00,59]
%p AM或者PM
%S 秒[00,61], 为什么不是[00,59],参考python手册
%U 周在当年的周数(是当年的第几周),星期天作为周的第一天;
%W 周在当年的周数(是当年的第几周),星期一作为周的第一天;
%w 今天在这周的天数[0,6],6表示星期天;
%x 日期字符串(如: 04/07/10)
%X 时间字符串(如: 10:43:39)
%y 2个数字表示的年份,不带世纪;
%Y 4个数字表示的年份,带世纪;
%z 与utc时间的间隔(如果是本地时间,返回空字符串)
%Z 时区名称(如果是本地时间,返回空字符串)
%% %%-->%
'''

'''时区的转换见pytz模块'''











































