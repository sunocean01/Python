'''
此脚本主要用来介绍pandas.timedelta()
'''
import pandas as pd


'''pandas.to_timedelta(arg, unit=None, errors='raise')'''
'''
arg：str, timedelta, list-like or Series，要转换为timedelta的数据
unit：str, optional，可选，表示数字arg的arg单位。默认为"ns"，在版本1.1.0中更改：arg上下文字符串和 时不能指定errors="raise"
    ‘W’
    ‘D’ / ‘days’ / ‘day’
    ‘hours’ / ‘hour’ / ‘hr’ / ‘h’
    ‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’
    ‘S’ / ‘seconds’ / ‘sec’ / ‘second’
    ‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’
    ‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’
    ‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’

errors：{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’，
    如果为“ raise”，则无效的解析将引发异常。
    如果为“强制”，则将无效解析设置为NaT。
    如果为“ ignore”，则无效的解析将返回输入。
'''
# pdTD = pd.to_timedelta('1 days 06:05:01.00003')
pdTD = pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan'])


print(pdTD)



