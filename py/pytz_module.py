import pytz
import datetime

'''此模块主要用来时区转换'''

# for i in dir(pytz):
    # print(i)
# exit()

'''pytz.country_timezones(‘国家代码’)：查看某个国家有哪些时区,国家代码请百度查找'''
# tz = pytz.country_timezones('SE')

'''pytz.timezone('Asia/Shanghai'):获取对应的时区信息,提供给datetime使用'''
# tzinfo = pytz.timezone('Asia/Shanghai')
# tz = datetime.datetime.now(tz=tzinfo)

'''pytz.all_timezones、common_timezones:查看有哪些时区,注意是属性,不带括号'''
# tz = pytz.all_timezones
# tz = pytz.common_timezones

'''
datetime.astimezone('目标时区'):将datetime转换成目标时区
运气比较好的是datetime.now()和utcnow()都带有时区功能, 如何将已知字符串时间如:"2021-02-16 09:00:00"添加山区信息,见下一条
'''
# # 不同时区之间互相转换
# tgtz = pytz.timezone('UTC')   #目标时区
# lotz = pytz.timezone('Asia/Shanghai')   #本地时区
# dt = datetime.datetime.now(tz=lotz)  #必须标记这个时间是哪个时区的,否则会报错为naive time(不明确的一个时间);
# tz = dt.astimezone(tz=tgtz)

# # UTC时间转换到其他时区
# tz = pytz.timezone('Asia/Shanghai')
# dt = datetime.datetime.utcnow()
# cst_time = tz.fromutc(dt).strftime("%Y-%m-%d %H:%M:%S")
# print(cst_time)

'''pytz.timezone('时区').localize("datetime时间")'''
# strtodt = datetime.datetime.strptime("2021-02-16 09:00:00","%Y-%m-%d %H:%M:%S")   #字符串时间-->datetime格式时间
# loctz = pytz.timezone("Asia/Shanghai")      #创建一个时区信息
# formatdt = loctz.localize(strtodt)          #将datetime时间格式化成带指定时区的时间

# tgtz = pytz.timezone('utc')
# coverttz = formatdt.astimezone(tz=tgtz)

# print("datetime格式时间:  ",strtodt)
# print("添加时区信息:      ",formatdt)
# print("转换成另外一个时区:",coverttz)
# exit()













print(tz)
exit()

# 获取0时区时间
D = datetime.datetime.utcnow()

'''时区转换:'''
# 设定一个目标时区
tz = pytz.timezone("Asia/Shanghai")

curtime = tz.fromutc(D)
print(D)
print(curtime)

