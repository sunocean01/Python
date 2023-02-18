'''此脚本主要用来介绍pivot_table()'''
import pandas as pd
import numpy as np

pd.options.display.max_columns = None
pd.options.display.max_rows = None


'''pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)'''
'''
data:       DataFrame
values:     column to aggregate, optional;聚合的列
index:      column, Grouper, array, or list of the previous; 在透视表索引上分组的键
            If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list). Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.

columns:    column, Grouper, array, or list of the previous
            If an array is passed, it must be the same length as the data. The list can contain any of the other types (except list). Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.

aggfunc:    function, list of functions, dict, default numpy.mean
            If list of functions passed, the resulting pivot table will have hierarchical columns whose top level are the function names (inferred from the function objects themselves) If dict is passed, the key is column to aggregate and value is function or list of functions.

fill_value:     scalar, default None
                Value to replace missing values with (in the resulting pivot table, after aggregation).

margins:        bool, default False, 是否对结果再做一个行或列方向的汇总
                Add all row / columns (e.g. for subtotal / grand totals).

dropna:         bool, default True
                Do not include columns whose entries are all NaN.

margins_name:       str, default ‘All’
                    Name of the row / column that will contain the totals when margins is True.

observed:           bool, default False
                    This only applies if any of the groupers are Categoricals. If True: only show observed values for categorical groupers. If False: show all values for categorical groupers.
'''


csv_path = r'C:\Users\osun\Desktop\Python\Function\testfile\FFmc0320210126.csv'


# '''Read file:'''
data = pd.read_csv(csv_path,header=0,index_col=None, nrows=10000,usecols=["Date","SoftBin","HardBin","T006001_1_Value","T006002_1_Value","T006036_1_Value","T006001_2_Value","T008016_Value","T008019_Value","T150001_Value","T004001_Value"])
# data = data.dropna(how='any')
data = data.rename(columns={"T006001_1_Value":"P25NumCo","T006002_1_Value":"MeanMass","T006036_1_Value":"ARZDecay","T006001_2_Value":"KCLNumCo","T008016_Value":"Omega","T008019_Value":"KCLGain","T150001_Value":"SetupId","T004001_Value":"DeviceId"})
data['Date'] = pd.to_datetime(data['Date']).dt.to_period('H')
data['Group'] = "AA"
data.iloc[::10,-1] = "BB"
data.iloc[::33,-1] = "CC"



'''每个pivot_table必须拥有一个index，如果想查看哈登对阵每个队伍的得分，首先我们将对手设置为index：'''
# data = pd.pivot_table(data,index=["Month","trade_date"])  
# data = pd.pivot_table(data,index=["trade_date","Month"])    #改变多层索引的顺序


'''values:可以对需要的计算数据进行筛选'''
# data = pd.pivot_table(data,index=["Month","trade_date"],values=["open","close","high","low"]) 


'''aggfunc: 可以设置我们对数据聚合时进行的函数操作'''
# data = pd.pivot_table(data,index=["Group"],values=["MeanMass","ARZDecay","KCLNumCo","Omega"],aggfunc=["sum","max","min","mean","count","median","prod","std","var"],margins=True)   #多列值
# data = pd.pivot_table(data,index=["Group"],values=["MeanMass","ARZDecay","KCLNumCo","Omega"],aggfunc={"MeanMass":"sum","ARZDecay":"min","KCLNumCo":"mean","Omega":"count"},columns=["SoftBin"],margins=True)   #aggfunc 传入字典,不同列应用不同函数
# data = pd.pivot_table(data,index=["Group"],values=["Omega"],aggfunc=["sum","max","min","mean","count","median","prod","std","var"],margins=True,margins_name="sum")             #只选omega列值
data = pd.pivot_table(data,index=["SetupId","Date"],values=["DeviceId"],aggfunc=["count"],columns=["SoftBin"],fill_value='',margins=True,margins_name="sum")             #统计每台设备每天不良情况

















print(data)