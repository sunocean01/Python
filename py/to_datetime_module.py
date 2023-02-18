'''
此脚本主要用来介绍pandas.datetime()
'''
import pandas as pd
import time

# 测试数据
# filepath = r'.\testfile\testdata.csv'
# data = pd.read_csv(filepath,index_col=0)
# data = data.set_index('Date')


# data = data[data['T004001_Value'].isin(['C11194516C5D1EB2'])]
# print(data)


'''pandas.to_datetime(arg, errors='raise', dayﬁrst=False, yearﬁrst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)'''
'''
1. arg ：[int, ﬂoat, str, datetime, list, tuple, 1-d array, Series DataFrame/dict-like] 
        The object to convert to a datetime.需要解析的对象，多种格式都可以
2. errors： [{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’]
        • If ‘raise’, then invalid parsing will raise an exception.
        • If ‘coerce’, then invalid parsing will be set as NaT.
        • If ‘ignore’, then invalid parsing will return the input.
3. dayﬁrst ：[bool, default False] 
        声明传入的参数前两位是天
        Specify a date parse order if arg is str or its list-likes. If True, parses dates with the day ﬁrst, eg 10/11/12 is parsed as 2012-11-10. Warning: dayﬁrst=True is not strict, but will prefer to parse with day ﬁrst (this is a known bug, based on dateutil behavior).
4. yearﬁrst： [bool, default False] 
        声明传入的参数前两位是年
        Specify a date parse order if arg is str or its list-likes.
        If True parses dates with the year ﬁrst, eg 10/11/12 is parsed as 2010-11-12.
        If both dayﬁrst and yearﬁrst are True, yearﬁrst is preceded (same as dateutil).
        Warning: yearﬁrst=True is not strict, but will prefer to parse with year ﬁrst (this is a knownbug, based on dateutil behavior).
5. utc： [bool, default None] 
        返回UTC时间格式
        Return UTC DatetimeIndex if True (converting any tz-aware date-time.datetime objects as well).
6. format： [str, default None] 
        The strftime to parse time, eg “%d/%m/%Y”, note that “%f” will parse all the way up to nanoseconds. See strftime documentation for more information on
        choices: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
7. exact： [bool, True by default] 
        Behaves as: - If True, require an exact format match. - If False,allow the format to match anywhere in the target string.
8. unit [str, default ‘ns’] 
        The unit of the arg (D,s,ms,us,ns) denote the unit, which is an integer or ﬂoat number. This will be based off the origin. Example, with unit=’ms’ and origin=’unix’ (the default), this would calculate the number of milliseconds to the unix epoch start. infer_datetime_format [bool, default False] If True and no format is given, attempt to infer the format of the datetime strings, and if it can be inferred, switch to a faster method of parsing them. In some cases this can increase the parsing speed by ~5-10x.
9. origin： [scalar, default ‘unix’] 
        Deﬁne the reference date. The numeric values would be parsed as number of units (deﬁned by unit) since this reference date.
        • If ‘unix’ (or POSIX) time; origin is set to 1970-01-01.
        • If ‘julian’, unit must be ‘D’, and origin is set to beginning of Julian Calendar. Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.
        • If Timestamp convertible, origin is set to Timestamp identiﬁed by origin.
10. cache： [bool, default True] 
        If True, use a cache of unique, converted dates to apply the datetime conversion. May produce signiﬁcant speed-up when parsing duplicate date strings, espe-cially ones with timezone offsets. The cache is only used when there are at least 50 values.
    The presence of out-of-bounds values will render the cache unusable and may slow down parsing.
'''

'''arg:需要解析的对象,多种格式都可以,包括时间戳都可以
基本是数据类型不限:[int, ﬂoat, str, datetime, list, tuple, 1-d array, Series dateFrame/dict-like] 
'''
# data.index = pd.to_datetime(data.index)   #将Indexs转换成datetime
# print(data.head())
# date = ["2020-12-01T08:14:57.162700+08:00",'2017-01-05 2:30:00', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105'] #各种字符串转换成datetime
# date = pd.to_datetime(date)
# -----------------------------------
'''errors:出现错误如何处理'''
'''
[{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’]
• If ‘raise’, 如果遇到无法转换的字符,pandas将报错.
• If ‘coerce’, 如果遇到无法转换的字符串,pandas将输出NaT.
• If ‘ignore’, 如果遇到无法解析的,pandas将字符串原样输出.
'''
# dates = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105', 'ABC']
# date = pd.to_datetime(dates,errors='coerce',utc=True)
# -----------------------
'''dayfirst:声明传入的前两位是天,'05/11/2020'如果不声明,默认是05月,只有有歧义的格式起作用,没有歧义的时间格式将忽视此参数,如'20200613'不管有没有此参数都会被解析为'2020-06-13' '''
'''
[bool, default False]
'05/11/2020':默认是2020-05-11
'20200613': 默认2020-06-13
'06132020': pandas是不认识的,需要指定格式format='%m%d%Y'
'''
# date = pd.to_datetime(['10/12/2020','05/11/2020','20200613'],dayfirst=True)
# ---------------
'''yearfirst:声明传入的前两位是年,针对于年的简写如: 2020 --> 20, 2019 --> 19'''
# date = pd.to_datetime(['201213','190715'],yearfirst=True)
# ----------------
'''utc:返回utc时间格式:2017-01-05 14:30:00+00:00'''
# date = pd.to_datetime(['10/12/2020','05/11/2020','20200613'],dayfirst=True,utc=True)
# date = pd.to_datetime(['10/12/2020 08:00:00','05/11/2020','20200613'],dayfirst=True)    #字符串的日期后面有带时间的,不用指定ute=True;
# ----------------------
'''format:非常重要的一个参数,告诉pandas提供的日期格式是什么样的'''
'''
"%Y-%m-%d %H:%M:%S"
如下面这个例子,如果不指定格式,pandas会报错;
'''
# date = pd.to_datetime(['05122020'],format='%m%d%Y')
# ----------------------

'''infer_datetime_format: True,pandas自己推断日期的格式顺序,好像没什么卵用'''

'''exact:日期格式是否需要严格匹配'''
'''
bool
'''
# -----------------------
'''unit:单位; 当传入的是时间戳时,要告诉你转入值的单位是什么'''
'''
[str, default ‘ns’] 
'''
# date = pd.to_datetime(1614143853.0919018,unit='s')
# ---------------------------------
'''将时间戳 --> 格林威治时间'''
# T = time.time()     #返回此时的时间戳
# date = pd.to_datetime(T,unit='s',utc=False)
# -------------------------------------------------

'''时区转换: 一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到别的时区了'''
# # tz_localize(): 本地化时区
# T = time.time()     #返回当前的时间戳,这个时间是UTC
# date = pd.to_datetime(T,unit='s',utc=False).tz_localize('UTC')  #这个地方已经是UTC时间,可以不用tz_localize()
# date = date.tz_convert("Asia/Shanghai")             #转换为上海时间
# date = date.tz_convert("America/New_York")
# date = date.tz_convert("Europe/Prague")             #瑞士时间

# date = pd.to_datetime('2021-02-16 10:30:00') #字符串时间转换成datetime格式
# date = date.tz_localize('Asia/Shanghai')   #添加时区信息,时区的名称,可以通过pytz.all_timezones 模块的方法获得;
# date = date.tz_convert("America/New_York")

# print(date)



