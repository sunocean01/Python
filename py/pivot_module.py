'''pivot用来重塑表格'''
import pandas as pd
import numpy as np

pd.options.display.max_columns = None
pd.options.display.max_rows = None

'''DataFrame.pivot(self, index=None, columns=None, values=None)→ 'DataFrame'
index: [str or object, optional] Column to use to make new frame’s index. If None, uses existing index.
columns: [str or object] Column to use to make new frame’s columns.
values: [str, object or a list of the previous, optional] Column(s) to use for populating new frame’s values. If not speciﬁed, all remaining columns will be used and the result will have hierarchically indexed columns.
'''

csv_path = r'C:\Users\osun\Desktop\Python\Function\testfile\FFmc0320210126.csv'


# '''Read file:'''
data = pd.read_csv(csv_path,header=0,index_col=None,usecols=["Date","SoftBin","HardBin","T006001_1_Value","T006002_1_Value","T006036_1_Value","T006001_2_Value","T008016_Value","T008019_Value","T150001_Value","T004001_Value"])
data = data.dropna(how='any')
data = data[['HardBin','SoftBin','T150001_Value']]
data = data.drop_duplicates('SoftBin')

'''注意要付给index的列里不能有重复项,否则报错'''
data_pivot = data.pivot(index='SoftBin',columns='T150001_Value',values='HardBin')
# data_pivot.reset_index(inplace=True)
print(data_pivot)