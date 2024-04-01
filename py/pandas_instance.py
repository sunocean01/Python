# -*- coding: utf-8 -*-
import pandas as pd
import sensirion_fastedf as sf
import matplotlib.pyplot as plt
import os
import time
import datetime
import re
import warnings

warnings.filterwarnings("ignore")   #可以将警告信息不显示

# %matplotlib inline
# %matplotlib notebook

pd.options.display.max_columns = None
pd.options.display.max_rows = None

'''下面两行解决无法显示中文的问题'''
import matplotlib
matplotlib.rc("font",family='YouYuan')

'''如果不加下面两句话，运行时会报警，也不知道为什么'''
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

'''如果没有下面这句话，在增加新列时会报错'''
pd.options.mode.chained_assignment = None




# '''Input the file path:'''
# edf_path = r"C:\work\PM2_5\LabSetup\2020_06\20200624T112050Z_Tool\20200624T112050Z_Tool_SPS3xCom_0F3283033AE2AE40.edf"
# # excel_path = r""

csv_path = r'.\testfile\002161.SZ.csv'


# '''Read file:'''
'''
filepath_or_buffer : str，pathlib。可以是URL，可用URL类型包括：http, ftp, s3和文件。对于多文件正在准备中
            本地文件读取实例：://localhost/path/to/table.csv
 
sep : str, default ‘,’,
            指定分隔符。如果不指定参数，则会尝试使用逗号分隔。分隔符长于一个字符并且不是‘\s+’,将使用python的语法分析器。并且忽略数据中的逗号。正则表达式例子：'\r\t'
 
delimiter : str, default None,定界符，备选分隔符（如果指定该参数，则sep参数失效）
 
delim_whitespace : boolean, default False.
            指定空格(例如’ ‘或者’ ‘)是否作为分隔符使用，等效于设定sep='\s+'。如果这个参数设定为Ture那么delimiter 参数失效。
 
header : int or list of ints, default ‘infer’
            指定行数用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。如果明确设定header=0 就会替换掉原来存在列名。header参数可以是一个list例如：[0,1,3]，这个list表示将文件中的这些行作为列标题（意味着每一列有多个标题），介于中间的行将被忽略掉（例如本例中的2；本例中的数据1,2,4行将被作为多级标题出现，第3行数据将被丢弃，dataframe的数据从第5行开始。）。
            注意：如果skip_blank_lines=True 那么header参数忽略注释行和空行，所以header=0表示第一行数据而不是文件的第一行。
 
names : array-like, default None
            用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None。默认列表中不能出现重复，除非设定参数mangle_dupe_cols=True。
 
index_col : int or sequence or False, default None
            用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。
            如果文件不规则，行尾有分隔符，则可以设定index_col=False 来是的pandas不适用第一列作为行索引。
 
usecols : array-like, default None
            返回一个数据子集，该列表中的值必须可以对应到文件中的位置（数字可以对应到指定的列）或者是字符传为文件中的列名。例如：usecols有效参数可能是 [0,1,2]或者是 [‘foo’, ‘bar’, ‘baz’]。使用这个参数可以加快加载速度并降低内存消耗。
 
as_recarray : boolean, default False
            不赞成使用：该参数会在未来版本移除。请使用pd.read_csv(...).to_records()替代。
            返回一个Numpy的recarray来替代DataFrame。如果该参数设定为True。将会优先squeeze参数使用。并且行索引将不再可用，索引列也将被忽略。
 
squeeze : boolean, default False
            如果文件值包含一列，则返回一个Series
 
prefix : str, default None
            在没有列标题时，给列添加前缀。例如：添加‘X’ 成为 X0, X1, ...
 
mangle_dupe_cols : boolean, default True
            重复的列，将‘X’...’X’表示为‘X.0’...’X.N’。如果设定为false则会将所有重名列覆盖。
 
dtype : Type name or dict of column -> type, default None
            每列数据的数据类型。例如 {‘a’: np.float64, ‘b’: np.int32}
 
engine : {‘c’, ‘python’}, optional
            使用的分析引擎。可以选择C或者是python。C引擎快但是Python引擎功能更加完备。
 
converters : dict, default None
            列转换函数的字典。key可以是列名或者列的序号。
 
true_values : list, default None
            Values to consider as True
            指定哪些值显示True,哪些值显示False
false_values : list, default None
            Values to consider as False
            指定哪些值显示True,哪些值显示False
skipinitialspace : boolean, default False
            忽略分隔符后的空白（默认为False，即不忽略）.
 
skiprows : list-like or integer, default None
            需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）。
 
skipfooter : int, default 0
            从文件尾部开始忽略。 (c引擎不支持)
 
skip_footer : int, default 0
            不推荐使用：建议使用skipfooter ，功能一样。
 
nrows : int, default None
            需要读取的行数（从文件头开始算起）。
 
na_values : scalar, str, list-like, or dict, default None
            一组用于替换NA/NaN的值。如果传参，需要制定特定列的空值。默认为‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘nan’`.
 
keep_default_na : bool, default True
            如果指定na_values参数，并且keep_default_na=False，那么默认的NaN将被覆盖，否则添加。
 
na_filter : boolean, default True
            是否检查丢失值（空字符串或者是空值）。对于大文件来说数据集中没有空值，设定na_filter=False可以提升读取速度。
 
verbose : boolean, default False
            是否打印各种解析器的输出信息，例如：“非数值列中缺失值的数量”等。
 
skip_blank_lines : boolean, default True
            如果为True，则跳过空行；否则记为NaN。
 
parse_dates : boolean or list of ints or names or list of lists or dict, default False
            boolean. True -> 解析索引
            list of ints or names. e.g. If [1, 2, 3] -> 解析1,2,3列的值作为独立的日期列；
            list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用
            dict, e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"
 
infer_datetime_format : boolean, default False
            如果设定为True并且parse_dates 可用，那么pandas将尝试转换为日期类型，如果可以转换，转换方法并解析。在某些情况下会快5~10倍。
 
keep_date_col : boolean, default False
            如果连接多列解析日期，则保持参与连接的列。默认为False。
 
date_parser : function, default None
            用于解析日期的函数，默认使用dateutil.parser.parser来做转换。Pandas尝试使用三种不同的方式解析，如果遇到问题则使用下一种方式。
            1.使用一个或者多个arrays（由parse_dates指定）作为参数；
            2.连接指定多列字符串作为一个列作为参数；
            3.每行调用一次date_parser函数来解析一个或者多个字符串（由parse_dates指定）作为参数。
 
dayfirst : boolean, default False
            DD/MM格式的日期类型
 
iterator : boolean, default False
            返回一个TextFileReader 对象，以便逐块处理文件。
 
chunksize : int, default None
            文件块的大小， See IO Tools docs for more informationon iterator and chunksize.
 
compression : {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}, default ‘infer’
            直接使用磁盘上的压缩文件。如果使用infer参数，则使用 gzip, bz2, zip或者解压文件名中以‘.gz’, ‘.bz2’, ‘.zip’, or ‘xz’这些为后缀的文件，否则不解压。如果使用zip，那么ZIP包中国必须只包含一个文件。设置为None则不解压。
            新版本0.18.1版本支持zip和xz解压
 
thousands : str, default None
            千分位分割符，如“，”或者“."
 
decimal : str, default ‘.’
            字符中的小数点 (例如：欧洲数据使用’，‘).
 
float_precision : string, default None
            Specifies which converter the C engine should use for floating-point values. The options are None for the ordinary converter, high for the high-precision converter, and round_trip for the round-trip converter.
            指定
 
lineterminator : str (length 1), default None
            行分割符，只在C解析器下使用。
 
quotechar : str (length 1), optional
            引号，用作标识开始和解释的字符，引号内的分割符将被忽略。
 
quoting : int or csv.QUOTE_* instance, default 0
            控制csv中的引号常量。可选 QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3)
 
doublequote : boolean, default True
            双引号，当单引号已经被定义，并且quoting 参数不是QUOTE_NONE的时候，使用双引号表示引号内的元素作为一个元素使用。
 
escapechar : str (length 1), default None
            当quoting 为QUOTE_NONE时，指定一个字符使的不受分隔符限值。
 
comment : str, default None
            标识着多余的行不被解析。如果该字符出现在行首，这一行将被全部忽略。这个参数只能是一个字符，空行（就像skip_blank_lines=True）注释行被header和skiprows忽略一样。例如如果指定comment='#' 解析‘#empty\na,b,c\n1,2,3’ 以header=0 那么返回结果将是以’a,b,c'作为header。
 
encoding : str, default None
            指定字符集类型，通常指定为'utf-8'. List of Python standard encodings
 
dialect : str or csv.Dialect instance, default None
            如果没有指定特定的语言，如果sep大于一个字符则忽略。具体查看csv.Dialect 文档
 
tupleize_cols : boolean, default False
            Leave a list of tuples on columns as is (default is to convert to a Multi Index on the columns)
 
error_bad_lines : boolean, default True
            如果一行包含太多的列(这一行比其他行的列多)，那么默认不会返回DataFrame ，如果设置成false，那么会将改行剔除（只能在C解析器下使用）。
 
warn_bad_lines : boolean, default True
            如果error_bad_lines =False，并且warn_bad_lines =True 那么所有的“bad lines”将会被输出（只能在C解析器下使用）。
 
low_memory : boolean, default True
            分块加载到内存，再低内存消耗中解析。但是可能出现类型混淆。确保类型不被混淆需要设置为False。或者使用dtype 参数指定类型。注意使用chunksize 或者iterator 参数分块读入会将整个文件读入到一个Dataframe，而忽略类型（只能在C解析器中有效）
 
buffer_lines : int, default None
            不推荐使用，这个参数将会在未来版本移除，因为他的值在解析器中不推荐使用
 
compact_ints : boolean, default False
            不推荐使用，这个参数将会在未来版本移除
            如果设置compact_ints=True ，那么任何有整数类型构成的列将被按照最小的整数类型存储，是否有符号将取决于use_unsigned 参数
 
use_unsigned : boolean, default False
            不推荐使用：这个参数将会在未来版本移除
            如果整数列被压缩(i.e. compact_ints=True)，指定被压缩的列是有符号还是无符号的。
memory_map : boolean, default False
            如果使用的文件在内存内，那么直接map文件使用。使用这种方式可以避免文件再次进行IO操作。
'''
data = pd.read_csv(csv_path,header=0,index_col=0, nrows=20,usecols=[1,2,3,4,5],
                    parse_dates=True,na_filter=True,infer_datetime_format=True,float_precision='high')

# data = pd.read_csv(csv_path,header=0,index_col=0,parse_dates=True,nrows=20,usecols=lambda x: x not in ['ts_code','vol','pre_close','change','pre_close','amount'])
# data = data.sort_index(axis=0,ascending=True)
print("Original Data:",data,'*'*80,sep='\n')



#1. 读取文件
"""
filepath_or_buffer：str, path object or file-like object 需要打开的文件路径
sep：            str, default ‘,’
                csv文件中每一行数据之间的分隔符。官方文档指出对于read_csv()这个参数默认是英文逗号’,’而对于read_table()这个参数默认是制表符‘|t’。当然用户可以根据自己csv文件格式的特点自行设置。read_csv()还有一个参数是 delimeter， 作用与sep相同，只不过delitemer的默认值为None，而不是英文逗号 ‘,’
delimiter：      str, default None
"""
# data = pd.read_csv(csv_path)

#2. header: 列标题设定
"""
header：         int, list of int, default ‘infer’
                指定行用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。如果明确设定header=0就会替换掉原来存在列名。header参数可以是一个list例如：[0,1,3]，这个list表示将文件中的这些行作为列标题（意味着每一列有多个标题），介于中间的行将被忽略掉
如：
header = None: 不设置列标，系统会默认设定为：0,1,2,3....
header = 0: 默认值，即将文件的第一行作为列标；
header = 2: 可以选择文件中的任意一行作为列标题；注：读取的数据是header以下的部分，header以上的部分不读取；
header = [2,3]: 可以同时选择任意多行作为列标题，如将第二行和第三行作为列标题，即多个标题
"""
# data = pd.read_csv(csv_path,header=0)

#3. names:自定义列标题
"""
names：          array-like, optional
                用于结果的列名列表(相当于自定义列标签)，如果数据文件中没有列标题行，就需要执行header=None。默认列表中不能出现重复，除非设定参数mangle_dupe_cols=True。
header在默认或者None的情况下：第一行会被保留；
header是数字的时候，如0，1，3... 的时候第一行不会被保留，也就是会被替代掉；
names = ['a','b','c','d']: 自定义列标题，当header是数字时替换header的内容
"""
# data = pd.read_csv(csv_path,header=0,names=['a','b','c','d','e'],nrows=20,usecols=[1,2,3,4,5])

#4. index_col: 行索引设定
"""
index_col：      int, str, sequence of int / str, or False, default None
                用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。
                如果文件不规则，行尾有分隔符，则可以设定index_col=False 来是的pandas不适用第一列作为行索引。

数字：即用第几列作为行标题；如：0,1,3
None: 默认，系统会设定0,1,2,3...多为行索引；
列名：哪一列的名称作为行索引；
列表：可以是列的位标或名称，如：[1,3,5]或['high','low']，也就是设定多个行标
False: 有点像None
"""
# data = pd.read_csv(csv_path,index_col=[0,3],nrows=20,usecols=[1,2,3,4,5])

#5. usecols: 选择需要读取的列
"""

usecols:        list-like or callable, optional
                也就是你可以选择性的打印相应的列；把不需要的列不打印；
                例如：usecols有效参数可能是 [0,1,2]或者是 [‘foo’, ‘bar’, ‘baz’]。使用这个参数可以加快加载速度并降低内存消耗
默认是读取全部列；
列表：可以是列的位标或名称，如[1,2,3,4,5]或者['trade_date','low','high']
"""
# data = pd.read_csv(csv_path,,nrows=20,usecols=[1,2,3,4,5])

#6.squeeze: 当文件只有一列的时候，是否返回Series
"""
squeeze：        bool, default False
                如果文件值包含一列，则返回一个Series
"""
# data = pd.read_csv(csv_path,usecols=['high'],squeeze=True)

#7. prefix：给列标题加前缀，只有在header=None时起作用，在不是None的情况下，不起作用，但也不会报错；
"""
prefix：         str, optional
                在没有列标题时，给列添加前缀。例如：添加‘X’ 成为 X0, X1, ...
注：只有在header=None时有效；
"""
# data = pd.read_csv(csv_path,header=None,nrows=20,usecols=[1,2,3,4,5],prefix='y')

#8. mange_dupe_cols: python3.5 提示不支持mangle_dupe_cols=False
"""
mangle_dupe_cols:   bool, default True
                    重复的列，将‘X’...’X’表示为‘X.0’...’X.N’。如果设定为false则会将所有重名列覆盖。
"""

#9. dtype: 指定列的数据类型
"""
dtype：          Type name or dict of column -> type, optional
                每列数据的数据类型。例如 {‘a’: np.float64, ‘b’: np.int32}
"""
# data = pd.read_csv(csv_path,nrows=20,usecols=[1,2,3,4,5],dtype={'trade_date':str,'open':str})
# print(data.dtypes)

#10. engine: 指定分析引擎，'c'或者'python'
"""
engine：         {‘c’, ‘python’}, optional
                使用的分析引擎。可以选择C或者是python。C引擎快但是Python引擎功能更加完备。
"""
# data = pd.read_csv(csv_path,nrows=20,usecols=[1,2,3,4,5],engine='c')

#11. converters: 在读取数据的时候，对列的数据进行变换，如此例中 'high'列，每个值增加2
"""
converters：     dict, optional
                列转换函数的字典。key可以是列名或者列的序号。
注：字典中的值必须是可迭代的
"""
# data = pd.read_csv(csv_path,nrows=20,usecols=[1,2,3,4,5],converters={'high': lambda x: float(x)+2})

#12. true_values/false_values:指定哪些值显示是True或者False,实测数字无效，字符串有效
"""
true_values:        list, optional
                Values to consider as True.
false_values:   list, optional
                Values to consider as False.
"""
# csv_path2 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test.csv'
# data = pd.read_csv(csv_path2,nrows=30,true_values=['A'],false_values=['B'])

#13. skipinitialspace：在行的最后有一个分隔符','，分隔符后面有空格，如果skipinitialspace=False,则显示' '，如果是True，则显示'NaN'
"""
skipinitialspace：bool, default False
                忽略分隔符后的空白（默认为False，即不忽略）.
"""
# csv_path2 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test.csv'
# data = pd.read_csv(csv_path2,nrows=30,skipinitialspace=True)

#14. skiprows:想过滤掉哪些行，就写在一个列表里面传递给skiprows即可。注意的是：这里是先过滤，然后再确定表头
"""
skiprows：       list-like, int or callable, optional
                需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）。
skiprows=3: 过滤掉前三行(包括表头)
skiprows=[1,3,5]: 过滤掉第1，3，5行
skiprows=lambda x: x > 0 and x % 2 == 0: 还可以传入lambda函数，筛选掉行号是偶数的行；
"""
# data = pd.read_csv(csv_path,nrows=20,skiprows=lambda x: x > 0 and x % 2 == 0)

#15. skipfooter:从文件末尾过滤行，解析引擎退化为 Python。这是因为 C 解析引擎没有这个特性。不能和nrows同时使用；
"""
skipfooter：     int, default 0
                从文件尾部开始忽略。 (c引擎不支持)
不能和nrows同时使用；
"""
# data = pd.read_csv(csv_path,engine='python',skipfooter=2980)

#16. nrows: 需要读取的行数，不包括列索引，先定header,然后选取nrows的行数；
"""
nrows：          int, optional
                需要读取的行数（从文件头开始算起）。
"""
# data = pd.read_csv(csv_path,header=0,nrows=3)

#17. na_values: 可以配置哪些值需要处理成 NaN
"""
na_values：      scalar, str, list-like, or dict, optional
                一组用于替换NA/NaN的值。如果传参，需要制定特定列的空值。默认为‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘nan’`.
na_values=8.00: 标量，具体的值；
na_values=[8.00,7.98]
na_values={'high':[8.11,7.98,7.8]}
"""
# data = pd.read_csv(csv_path,header=0,nrows=20,na_values={'high':[8.11,7.98,7.8]})

#18. keep_default_na: 原始文件中的空值是否显示为'NaN', True:显示；False:不显示；当使用na_values时，keep_default_na可以配合区分哪些是原始文件的空值，哪些是替换的；
"""
keep_default_na：bool, default True
                如果指定na_values参数，并且keep_default_na=False，那么默认的NaN将被覆盖，否则添加。
                Whether or not to include the default NaN values when parsing the data. Depending on whether na_values is passed in, the behavior is as follows:
                ® If keep_default_na is True, and na_values are specified, na_values is appended to the default NaN values used for parsing.
                ® If keep_default_na is True, and na_values are not specified, only the default NaN values are used for parsing.
                ® If keep_default_na is False, and na_values are specified, only the NaN values specified na_values are used for parsing.
                ® If keep_default_na is False, and na_values are not specified, no strings will be parsed as NaN.
                Note that if na_filter is passed in as False, the keep_default_na and na_values parameters will be ignored.
"""
# csv_path2 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test.csv'
# data = pd.read_csv(csv_path2,header=0,nrows=20,keep_default_na=True)

#19. na_filter, bool,虽然值为False时可以提升读取速度,但是notna()函数不可用:数据里的空值找不出来
"""
na_filter：      bool, default True
                是否检查丢失值（空字符串或者是空值）。对于大文件来说数据集中没有空值，设定na_filter=False可以提升读取速度。
"""
#20.verbose：
"""
verbose：        bool, default False
                是否打印各种解析器的输出信息，例如：“非数值列中缺失值的数量”等。
"""

#21. skip_blank_lines：是否跳过空行，否则NaN
"""
skip_blank_lines：   bool, default True
                如果为True，则跳过空行；否则记为NaN。
"""
# csv_path2 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test.csv'
# data = pd.read_csv(csv_path2,header=0,nrows=20,skip_blank_lines=True)

#22. parse_dates: 将列解析成日期格式
"""
parse_dates：    bool or list of int or names or list of lists or dict, default False
布尔值boolean：是否将索引解析成日期，True:解析;False:不解析；
列表：         列的位置或名称列表: e.g. If [1, 2, 3]或['date'] -> 解析1,2,3列或‘date'列的值作为独立的日期列；
嵌套的列表：      list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用；
字典dict：      e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"；
Note: A fast-path exists for iso8601-formatted dates.
"""
# data = pd.read_csv(csv_path,header=0,nrows=20,parse_dates=['trade_date'])

#23. infer_datetime_format: parse_dates的加速器
"""
infer_datetime_format：  bool, default False
                如果设定为True并且parse_dates可用，那么pandas将尝试转换为日期类型，如果可以转换，转换方法并解析。在某些情况下会快5~10倍。
"""
# data = pd.read_csv(csv_path,header=0,nrows=20,parse_dates=['trade_date'],infer_datetime_format=True)

#24. keep_date_col：如果连接多列解析日期，则保持参与连接的列。
"""
keep_date_col：  bool, default False
                如果连接多列解析日期，则保持参与连接的列。默认为False。
"""

#25. date_parser：有些时间格式比较特别，需要我们告诉系统我是什么样的时间格式，系统才可以解析，如'2018年1月1日'
"""
date_parser：    function, optional
                用于解析日期的函数，默认使用dateutil.parser.parser来做转换。Pandas尝试使用三种不同的方式解析，如果遇到问题则使用下一种方式。
                1.使用一个或者多个arrays（由parse_dates指定）作为参数；
                2.连接指定多列字符串作为一个列作为参数；
                3.每行调用一次date_parser函数来解析一个或者多个字符串（由parse_dates指定）作为参数。
date_parser 参数定制某种时间类型，详细使用过程总结如下。因为有些格式虽然是日期，但不是那种可以直接转换的样子：比如‘2018-01-01‘。可能是这种类型：‘2018年1月1日‘，这个时候我们就需要手动来定制解析的规则
df = pd.read_csv("xx.csv", parse_dates=["column"], date_parser=lambda x: pd.datetime.strptime(x, "%Y年%m月%d日"))
"""                

#26. dayfirst：当日期格式有歧义时，告诉pandas 第一个数字是不是天，比如：10092020
"""
dayfirst：       bool, default False
                DD/MM格式的日期类型
                DD/MM format dates, international and European format.
"""
# csv_path8 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test6.csv'
# data = pd.read_csv(csv_path8,index_col=1,parse_dates=True,dayfirst=True)

#27. cache_dates：
"""
cache_dates：    bool, default True
                If True, use a cache of unique, converted dates to apply the datetime conversion. May produce significant speed-up when parsing duplicate date strings, especially ones with timezone offsets.
                New in version 0.25.0.
"""

#28. iterator: 对大文件进行分批读入
"""
iterator：       bool, default False
                返回一个TextFileReader 对象，以便逐块处理文件。类似迭代器对象；
                Return TextFileReader object for iteration or getting chunks with get_chunk().
iterator取值boolean，默认为False。如果为True，那么返回一个TextFileReader对象，以便逐块处理文件。这个在文件很大时，内存无法容纳所有数据文件，此时分批读入，依次处理。
"""

# chunk = pd.read_csv(csv_path,iterator=True)  
# loop = True
# while loop:
    # try:
        # print(chunk.get_chunk(100))
    # except StopIteration:
        # loop = False
        # print('Finish iteration')

#29. chunksize: 功能类似iterator，传入参数后，都要用get_chunk()函数
"""
chunksize：      int, optional
                文件块的大小， See IO Tools docs for more informationon iterator and chunksize.
                Return TextFileReader object for iteration. See the IO Tools docs for more information on iterator and chunksize.
"""
# chunk = pd.read_csv(csv_path,chunksize=100)
# loop = True
# while loop:
    # try:
        # print(chunk.get_chunk())
    # except StopIteration:
        # loop= False
        # print('Finish')

#30. compression: 直接读取被压缩的csv文件
"""
compression：    {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}, default ‘infer’
                直接使用磁盘上的压缩文件。如果使用infer参数，则使用 gzip, bz2, zip或者解压文件名中以‘.gz’, ‘.bz2’,‘.zip’,or‘xz’这些为后缀的文件，否则不解压。如果使用zip，那么ZIP包中国必须只包含一个文件。设置为None则不解压。
                新版本0.18.1版本支持zip和xz解压
"""
# csv_path3 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ.csv.zip'
# data = pd.read_csv(csv_path3,compression='zip',nrows=20)

#31. thousands：将带有千分位','的字符串数字转换成整型或浮点型数据；
"""
thousands：      str, optional
                千分位分割符，如“，”或者“."
                Thousands separator.
"57,575.081"类似这种带有千分位的数字在存储时只能以字符串格式存储，读取的时候如果想给转换成整型或浮点型，则传入此参数：thousands=',';
"""
# csv_path4 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test2.csv'
# data = pd.read_csv(csv_path4,nrows=20,thousands=',')

#32. decimal:指定小数点类型，还不熟悉怎么用
"""
decimal：        str, default ‘.’
                字符中的小数点 (例如：欧洲数据使用',').
"""
# data = pd.read_csv(csv_path4,nrows=20,decimal=',')

#33. lineterminator: 把什么作为换行符，'\n','\t','\r',','...,
"""
lineterminator：str (length 1), optional
                行分割符，只在C解析器下使用。
"""
# data = pd.read_csv(csv_path4,nrows=20,lineterminator='\n')

#34: quotechar: ???
"""
quotechar：      str (length 1), optional
                引号，用作标识开始和解释的字符，引号内的分割符将被忽略。
quoting：        int or csv.QUOTE_* instance, default 0
                控制csv中的引号常量。可选 QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3)
doublequote：    bool, default True
                双引号，当单引号已经被定义，并且quoting 参数不是QUOTE_NONE的时候，使用双引号表示引号内的元素作为一个元素使用。
escapechar:     str (length 1), optional
                当quoting 为QUOTE_NONE时，指定一个字符使的不受分隔符限值。
                One-character string used to escape other characters.
"""

#35: comment：注释的内容要不要打印出来；头部如果有超过2行注释的话，在需要打印出来的时候会报错；
"""
comment：        str, optional
                标识着多余的行不被解析(就是注释的部分要不要打印出来)。如果该字符出现在行首，这一行将被全部忽略。这个参数只能是一个字符，空行（就像skip_blank_lines=True）注释行被header和skiprows忽略一样。例如如果指定comment='#' 解析‘#empty\na,b,c\n1,2,3’ 以header=0 那么返回结果将是以’a,b,c'作为header。
文件中有#开头的注释内容，如果不传入comment参数，注释部分将会被打印出来，如果设定comment='#',那么#后面的内容将不会被打印出来；
"""
# csv_path5 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test3.csv'
# data = pd.read_csv(csv_path5,comment='#')

#36. encoding/dialect:通常指定为 ‘utf-8‘。根据情况也可能是ISO-8859-1
"""
encoding：       str, optional
                指定字符集类型，通常指定为'utf-8'. List of Python standard encodings
dialect：        str or csv.Dialect, optional
                如果没有指定特定的语言，如果sep大于一个字符则忽略。具体查看csv.Dialect 文档
"""

#37. error_bad_lines/warn_bad_lines: 这两个需要配合使用，比如文件应该有3列，但是有些行却有4个数据，默认情况下会报错，但是我们可以设置成error_bad_lines=False(把有错误的行剔除掉),warn_bad_lines=True(将踢除掉的行打印出来);
"""
error_bad_lines：bool, default True
                如果一行包含太多的列，那么默认不会返回DataFrame ，如果设置成false，那么会将改行剔除（只能在C解析器下使用）。
warn_bad_lines：bool, default True
                如果error_bad_lines =False，并且warn_bad_lines =True 那么所有的“bad lines”将会被输出（只能在C解析器下使用）。
如果一行包含过多的列，假设csv的数据有3列，但是某一行却有4个数据，显然数据有问题。那么默认情况下不会返回DataFrame，而是会报错。 
# pandas.errors.ParserError: Error tokenizing data. C error: Expected 3 fields in line 3, saw 4
我们在某一行中多加了一个数据，结果显示错误。因为girl.csv里面有三列，但是有一行却有四个数据，所以报错。
在小样本读取时，这个错误很快就能发现。但是如果样本比较大、并且由于数据集不可能那么干净、很容易出现这种情况，那么该怎么办呢？而且这种情况下，Excel基本上是打不开这么大的文件的。这个时候我们就可以将error_bad_lines设置为False(默认为True)，意思是遇到这种情况，直接把这一行给我扔掉。同时会设置 warn_bad_lines 设置为True，打印剔除的这行。
"""
# csv_path6 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test4.csv'
# data = pd.read_csv(csv_path6,error_bad_lines=False,warn_bad_lines=True)

#38. delim_whitespace: 是否将空格' '作为分隔符
"""
delim_whitespace:   bool, default False
                Specifies whether or not whitespace (e.g. ' ' or '    ') will be used as the sep. Equivalent to setting sep='\s+'. If this option is set to True, nothing should be passed in for the delimiter parameter.
"""
# csv_path7 = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ_test5.csv'
# data = pd.read_csv(csv_path7,delim_whitespace=True)
# print(data.shape)

#39. low_memory: DataFrame在读取文件时默认是True:文件分块读取;可以设置成False:一次读取整个文件，避免类型混淆错误；
"""
low_memory：     bool, default True
                 分块加载到内存，再低内存消耗中解析。但是可能出现类型混淆。确保类型不被混淆需要设置为False。或者使用dtype参数指定类型。注意使用chunksize或者iterator参数分块读入会将整个文件读入到一个Dataframe，而忽略类型（只能在C解析器中有效）
这个看起来是和内存有关的，但其实它是和数据类型相关的。在解释这个原因之前，我们还要先从DataFrame的数据类型说起。
我们知道得到DataFrame的每一列都是有类型的，那么在读取csv的时候，pandas也是要根据数据来判断每一列的类型的。但pandas主要是靠"猜"的方法，因为在读取csv的时候是分块读取的，每读取一块的时候，会根据数据来判断每一列是什么类型；然后再读取下一块，会再对类型进行一个判断，得到每一列的类型，如果得到的结果和上一个块得到结果不一样，那么就会发出警告，提示有以下的列存在多种数据类型：
#DtypeWarning: Columns (1,5,8,......) have mixed types. Specify dtype option on import or set low_memory=False.
而为了保证正常读取，那么会把类型像大的方向兼容，比如第一个块的user_id解释成整型，但是第二个块发现user_id有的值无法解析成整型的，那么类型整体就会变成字符串，于是pandas提示该列存在混合类型。而一旦设置low_memory=False，那么pandas在读取csv的时候就不分块读了，而是直接将文件全部读取到内存里面，这样只需要对整体进行一次判断，就能得到每一列的类型。但是这种方式也有缺陷，一旦csv过大，就会内存溢出。
但是从数据库读取就不用担心了，因为数据库是规定了每一列的类型的。如果是从数据库读取得到的DataFrame，那么每一列的数据类型和数据库表中的类型是一致的。
还有，我们在上面介绍了dtype，这个是我们手动规定类型。那么pandas就会按照我们规定的类型去解析指定的列，但是一旦无法解析就会报错。
"""
#40. memory_map: 数据如果已经在内存中了，直接进行映射即可，不需要再次I/O
"""
memory_map:     bool, default False
                If a filepath is provided for filepath_or_buffer, map the file object directly onto memory and access the data directly from there. Using this option can improve performance because there is no longer any I/O overhead.
如果你知道python的一个模块mmap，那么你肯定很好理解。如果使用的数据在内存里，那么直接进行映射即可，不会再次进行IO操作。默认为False
"""
# csv_path = r'C:\Users\osun\Desktop\Python\00_my_script\40_Stock\database\qfq\002161.SZ.csv'
# with open(csv_path,'r+') as f:
    # data = pd.read_csv(f,memory_map=True,nrows=30)

#41. float_precision: 
"""
float_precision:    str, optional
                    Specifies which converter the C engine should use for floating-point values. 
                    The options are:
                    None: for the ordinary converter, 
                    high: for the high-precision converter, 
                    round_trip: for the round-trip converter.
"""
# data = pd.read_excel(excel_path)
'''
1、io，Excel的存储路径
2、sheet_name，要读取的工作表名称
	可以是整型数字、列表名或SheetN，也可以是上述三种组成的列表。
	2.1 整型数字：目标sheet所在的位置，以0为起始，比如sheet_name = 1代表第2个工作表。
	2.2 列表名：目标sheet的名称，中英文皆可。
        data = pd.read_excel(io, sheet_name = '英超射手榜')
	2.3 SheetN：代表第N个sheet，S要大写，注意与整型数字的区别。
        data = pd.read_excel(io, sheet_name = 'Sheet5')
	2.4 组合列表： sheet_name = [0, '英超射手榜', 'Sheet4']，代表读取三个工作表，分别为第1个工作表、名为“英超射手榜”的工作表和第4个工作表。显然，Sheet4未经重命名。
	sheet_name 默认为0，取Excel第一个工作表。如果读取多个工作表，则显示表格的字典。对于初学者而言，建议每次读取一个工作表，然后进行二次整合。
	data = pd.read_excel(io, sheet_name = ['英超积分榜', '西甲积分榜'], nrows = 5)
	sheet_name = ['英超积分榜', '西甲积分榜'] ，返回两个工作表组成的字典
3、header， 用哪一行作列名
    默认为0 ，如果设置为[0,1]，则表示将前两行作为多重索引。
4、names， 自定义最终的列名
    一般适用于Excel缺少列名，或者需要重新定义列名的情况。
    注意：names的长度必须和Excel列长度一致，否则会报错。
5、index_col， 用作索引的列
    可以是工作表列名称，如index_col = '排名'；
    可以是整型或整型列表，如index_col = 0 或 [0, 1]，如果选择多个列，则返回多重索引。
6、usecols，需要读取哪些列
    可以使用整型，从0开始，如[0,2,3]；
    可以使用Excel传统的列名“A”、“B”等字母，如“A：C, E” ="A, B, C, E"，注意两边都包括。
7、squeeze，True/False 当数据仅包含一列
8、converters ，强制规定列数据类型
    converters = {'排名': str, '场次': int}， 将“排名”列数据类型强制规定为字符串（pandas默认将文本类的数据读取为整型），“场次”列强制规定为整型；
9、skiprows，跳过特定行
    skiprows= n， 跳过前n行； skiprows = [a, b, c]，跳过第a+1,b+1,c+1行（索引从0开始）；
10、nrows ，需要读取的行数
11、skipfooter ， 跳过末尾n行
'''
# data = sf.read_edf(edf_path)

#取单列/多列：data.xx; data[];data.loc[];data.iloc[]
# data = data.open                      #取单列
# data = data['close']                  #取单列
# data = data.loc[:,'close']            #取单列
# data = data.iloc[:,2]                 #取单列
# data = data[['close','open']]         #取多列
# data = data.loc[:,['close','open']]   #取多列
# data = data.loc[:,'open':'low']       #取连续多列
# data = data.iloc[:,[1,3]]             #取多列
# data = data.iloc[:,1:4]               #取连续多列

#取行:data[]：类似已经将行索引的位置号已经放在一个列表里了，对列表进行取值，只是类似[3]([]放单个数)不可用，[]中必须有冒号':'
# data = data[2:5]                                  #取第3~5行
# data = data[-10:-3:2]                             #取行，从上往下取，步幅为2
# data = data[::-1]                                 #取行，逆序(从下往上取)
# data = data.loc['2020-08-14']                     #取单行
# data = data.loc['2020-08-14']                     #当日期被解析成日期格式时，需要以字符串形式索引
# data = data.loc[20200814]                         #取单行,行索引为float型，日期没有解析的情况下形式
# data = data.loc[[20200814,20200812]]              #取单行/多行,返回DataFrame,当索引数值类型是非时间格式有效
# data = data.loc['2020-08-14':'2020-08-10']        #取多行
# data = data.iloc[2]                               #取单行，data.iloc[]和data[]类似，比data[]更强大；
# data = data.iloc[2:10:2]                          #取多行，还可以增加步幅
# data = data.iloc[-10:-2:2]                        #还可以从下往上取
# data = data.iloc[[1,3,6]]                         #取多行，指定的多行

#取块(查询)/片/域
# data = data.at['2020-08-19','close']              #取单个值，只能取单个值，放在列表里
# data = data.iat[2,2]                              #取单个值，只能取单个值，返回单个值
# data = data.open['2020-08-18']                    #取单个值，返回DataFrame，基于取得列的基础上；
# data = data.open['2020-08-18':'2020-07-30']       #取单列连续多行，返回DataFrame，基于取得列的基础上；
# data = data.open[[1,3,4,8]]                       #取多个值，返回DataFrame，基于取得列的基础上；
# data = data['open']['2020-08-18']                 #取单个值，返回DataFrame，基于取得列的基础上；
# data = data[['open','close']]['2020-08-18']
# data = data.loc['2020-08-19','high']              #取单个值，返回DataFrame
# data = data.iloc[2,2]                             #取单个值，返回单个值
# data = data.loc[:,'open']['2020-08-18']           #取单个值，返回DataFrame，基于取得列的基础上；
# data = data.iloc[:,2]['2020-08-18']               #取单个值，返回DataFrame，基于取得列的基础上；
# data = data['open']['2020-08-18':'2020-08-13']    #取块，返回DataFrame，基于取得列的基础上；
# data = data.loc['2020-08-19':'2020-08-12','open':'low']       #取块，连续行连序列
# data = data.loc[[20200819,20200804],['open','low']] #取块，指定行指定列，行索引是时间类型的情况下不可用，已验证整型和字符串的行索引可用
# data = data.iloc[2:10,1:4]                        #取块，通过位置指定行指定列
# data = data.iloc[[5,10],[1,3]]                    #指定多行多列

#按条件取值/查询
'''
条件表达式(>, but also ==, !=, <, <=,. . . would work)实际是一个pandas Series与原DataFrame有相同行数的布尔值，这些布尔值用来筛选DataFrame,仅仅布尔值是True对应的行会被返回；
'''
# data = data[data['close']>7.8]                 #取close列大于7.8的所有行
# data = data.loc[data['close']>14.8]
# data = data.loc[data['close']>14.8,:]
# data = data.loc[data['close']>7.8,['high','open','close']]  #当条件满足时取对应的行及指定的列
# data = data[data > 8]                          #不符合条件的项会被置空，data里面的数据必须是整型或浮点型，不能是字符串；
# data = data[data == 7.99]                   #查找值为7.99的元素，查找结果只有一个，返回的是带行索引
# data = data[data.close.between(7.8,8.1)]
# query函数更简洁,见query函数介绍

'''~按位取反'''
# data['Note'] = data.apply(lambda x: 'AA' if x.open>8 else 'BB',axis=1)
# data = data[~data['Note'].str.startswith('A')]



'''isin():查'''
# data = data[data.index.isin(['2020-08-18','2020-08-13','2020-07-30','2020-08-16'])]  #按照给定的清单进行查，注意当trade_date作为列索引时需要用data.index.
# data = data.loc[data.index.isin(['2020-08-18','2020-08-13','2020-07-30'])]
# data = data.loc[data.close.isin([7.99,8.01])]

'''增加列'''
# data['Per'] = (data.close-data.open)/data.open*100        #直接赋值
# data.loc[:,'amplitude'] = data['high'] - data['low']      #直接赋值
# data.loc[data.close>8,'Note'] = 'AAA'                     #按条件赋值，将close值大于8的标记为’AAA‘

# data = data.loc[data['close'].notna()]                    #只取非空的数值,read_csv()里的na_filter=True时notna()才可以用
# data = data[data.close.notna()]

'''assign: 增加新的列，列名是关键字，可用同时增加任意多列'''
'''
**kwargs : dict of {str: callable 或 Series}
列名是关键字。如果这些值是可调用的，那么它们将在DataFrame上计算并分配给新列。可调用项不能更改输入DataFrame(不过pandas不会检查它)。
如果这些值是不可调用的(例如，Series、scalar或array)，则只分配它们。
'''
# data = data.iloc[0:5]
# data = data.assign(Deviation=lambda x:x.close-x.open,Note2='DDD')  #这里的lambda传入的是DataFrame的每一行；
'''# data = data.assign(Group=lambda x:"AAA" if x.close>x.open else "BBB")  #这里lambda不可以条件赋值, 原因?
原因: x 是每一列的数据, x.close>x.open 是serial,
'''

# --------------------------------------------------------------------------
# def Note(x):
    # if x.close>8.00:
        # return 'AAA'
    # elif x.close<8.00:
        # return 'BBB'
    # else:
        # return 'CCC'

'''apply：对DataFrame每行或者每列进行函数应用,可以用来进行条件赋值'''
# data['Note'] = data.apply(Note,axis=1)           #axis=1,表示将每一行的数据作为series数据结构传递给Note函数；
# data['Note'] = data.apply(lambda x: 'AAA' if x.close>8 else ("BBB" if x.close<8 else "CCC"),axis=1)  #lambda多条件判断

# data['sum'] = data.apply(lambda x: x.sum(),axis=1)                        #对每一行求和

# sum = data.apply(lambda x: x.sum(),axis=0).to_frame().T                  #对每一列求和后，转换成DataFrame,并转置
# sum = sum.rename(index={0:'sum'})                                        #对行索引该名字
# data = data.append(sum)                                                  #将结果放在最后一行
# --------------------
'''map:series属性，对series里的每一个值进行函数应用，DataFrame无map属性'''
# data['Note'] = data.open.map(lambda x: 'AA' if x>8 else 'bb')
# ------------------------
'''applymap: 对DataFrame中的每一个值进行应用函数'''
# data = data.applymap(lambda x: x+3)     #同 data =  data + 3               #DataFrame中的每个值加3
# data = data.applymap(lambda x: "#"+str(x))                                 #这个就不是data+3可用实现的了；
# -------------------


'''dropna:删除空值'''
'''
axis : {0 or 'index', 1 or 'columns'}, default 0
        0, or 'index'：删除包含丢失值的行
        1, or 'columns'：删除包含丢失值的列
         默认为0
how : {'any', 'all'}, default 'any'
        'any': 如果存在NA值，则删除该行或列
        'all': 如果所有值都是NA，则删除该行或列
thresh: int,保留含有int个非空值的行
subset: 对特定的列进行缺失值删除处理
'''
# data = data.dropna(how='any')                                              #删除所有缺失数据的行；
# -------------------------------------
'''drop:删除行/列'''
'''
labels: str, list;
axis=0，指删除index，因此删除columns时要指定axis=1；
inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新dataframe；
inplace=True，则会直接在原数据上进行删除操作，删除后就回不来了。
'''
# data = data.drop(['open','high'],axis=1)           #Both:删除指定的行或列，返回新的DataF
# -------------------------------
'''drop_duplicates:删除重复的值'''
'''
subset： 列名，可选，默认为None
keep： {‘first’, ‘last’, False}, 默认值 ‘first’
    •first： 保留第一次出现的重复行，删除后面的重复行。
    •last： 删除重复项，除了最后一次出现。
    •False： 删除所有重复项。
inplace：布尔值，默认为False，是否直接在原数据上删除重复项或删除重复项后返回副本。（inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本
'''
# data = data.drop_duplicates()           #Both:去除重复的行
# -------------------------------------
'''pop:返回item并从frame中删除。如果找不到，会引发KeyError。'''
'''
item ：str,要pop出的列的标签。

''' 
# dt = data.pop('low')                    #Both:返回low并从frame中删除。
# print(dt)
# -----------------------
'''补'''
'''
value: 要填充的值
    value = 100, 所有的空值都被替换成指定的值
    value = {'open':10,'high':110},对不同的列填充不同的值
inplace: bool
method: 'ffill','bfill'
    'ffill': 用上一个值来填充；
    'bffill': 用下面一个值进行填充；
limit: int, 传入每一列需要被填充的次数；
axis：0('index'),1('columns'), 填充的方向；默认0
'''
# # data = data.fillna({'open':10,'high':110},limit=1)
# -----------------------------------

'''DataFrame/Series Attributes属性'''
# data = data.T                             #Both:转置
# data = data.close.array                   #Series:转成数组
# data = data.axes                          #Both:返回行标的列表，index返回的是series；
# data = data.index                         #同axes
# data = data.columns                       #DataFrame:返回列标签，indexs数据类型
# data = data.keys()                        #Both:等同与data.columns
# data = data.close.dtype                   #Series:返回series数据的属性
# data = data.dtypes                        #Both:返回数据的属性，可以用于series和DataFrame, 有s是复数
# data = data.empty                         #Both:判断DataFrame是否为空
# data = data.open.hasnans                  #Series：判断是否有空值
# data = data.close.is_monotonic_increasing #Series:检测列是否为单调增加
# data = data.close.is_monotonic_decreasing   #Series:检测列是否为单调增减
# data = data.apply(lambda x: x.is_monotonic_increasing,axis=0)      #DataF:对每一列进行检测是否为单调增加
# data = data.open.is_unique                #Series:检测对象里的元素是否都是唯一的, data.index.is_unique, data.close.unique: 返回唯一值
# print(data.close.nbytes)                  #Series:返回存储给定对象的基础数据所需的字节数
# print(data.ndim)                          #Both:返回数据的维数
# print(data.shape)                         #Both:返回表格的 （行x列）
# data = data.size                          #Both:返回元素的个数
# data = data.values                        #Both:返回元素的值列表,DataFrame转换成数组

'''方法'''
'''abs():返回绝对值'''
# data = data.abs()                         #Both:返回绝对值
# --------------------------------
'''add: 等价于dataframe + other，但是支持用fill_value替换其中一个输入中缺失的数据。使用反向版本，radd。'''
'''
other : scalar, sequence, Series, 或 DataFrame 任何单个或多个元素数据结构，或类似列表对象。
axis : {0 或 ‘index’, 1 或 ‘columns’} 不论通过index(0 或 ‘index’)或columns(1 or ‘columns’)进行比较。 对于Series输入，axis匹配Series索引。
level : int 或 label 跨level广播，匹配传递的MultiIndex level的索引值。
fill_value : float 或 None, 默认 None 在计算之前，用这个值填充现有的缺失值(NaN)，以及成功进行DataFrame对齐所需的任何新元素。
如果两个对应的DataFrame位置中的数据都丢失，则结果将丢失。
'''
# data = data.iloc[:5]
# data = data.add([10,20,10,20,100],axis=0)                   #Both:在Series/DataF上面加上任何单个或多个元素数据结构，或类似列表对象
# ------------------
'''add_prefix/add_suffix: 给列名加前缀/后缀'''
'''
prefix : str,要在每个标签前添加的字符串。
'''
# data = data.add_prefix('TK_')             #Both:给标签加前缀,Series:给行标加；DataF:给列标加
# data = data.add_suffix('_TK')             #Both:给标签加后缀,Series:给行标加；DataF:给列标加
# -----------------------------------------------------------------------
'''agg:函数聚合'''
'''
func : function, str, list 或 dict 函数，用于聚合数据。如果是函数，则必须在传递DataFrame或传递到DataFrame.apply时工作。
接受的组合是:
1. function
    func = max或'max' ,好像要不要引号都可以
2. string function name
    ?
3. functions的list  和/或 function names, 例如， 
    func=[np.sum, 'mean',min], 函数名称上面有没有引号都可以;
4. axis labels的dict -> functions, function names 或 这样的list. 对不同的列应用不同的函数;
    func = {'open':[sum,max],'close':[min,'mean']}, 这里的'mena'需要用引号,不知道为啥
axis : {0 or ‘index’, 1 或 ‘columns’}, 默认 0 如果0或' index ':应用函数到每一列。如果1或‘columns’:应用函数到每一行。
*args
要传递给func的位置参数。
**kwargs
要传递给func的关键字参数。
'''
# data = data.agg(func={'open':[max,'min'],'close':[sum,'mean']},axis=0)    #Both:函数聚合
# ------------------
'''align:对比两个DataF/series,只区分对应的位置是否有值,不区分具体的值是否相同'''
'''
other : DataFrame 或 Series
join : {‘outer’, ‘inner’, ‘left’, ‘right’}, 默认 ‘outer’
    inner: 取交集
    outer: 取并集
axis : 允许另一个对象的axis, 默认 None 对齐 index (0), columns (1), 或 both (None)
level : int 或 level name, 默认 None 跨level广播，匹配传递的多索引level上的索引值
copy : boolean, 默认 True 始终返回新对象。如果copy = False并且不需要重建索引，则返回原始对象。
fill_value : scalar, 默认 np.NaN 用于缺失值的值。默认为NaN，但可以是任何“兼容”值。
method : {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, 默认 None 用于reindexed Series pad的填充孔的方法/ffill：将最后有效观察向前传播到下一个有效backfill / bfill：使用NEXT有效观察来填补空白
limit : int, 默认 None 如果指定了method，则这是向前/向后填充的连续NaN值的最大数量。换句话说，如果存在超过此数量的连续NaN的间隙，则仅部分填充。如果未指定method，则这是沿整个轴填充NaN的最大条目数。如果不是None，则必须大于0。
fill_axis : {0 or ‘index’, 1 or ‘columns’}, 默认 0
Filling axis, method 或 limit
broadcast_axis : {0 或 ‘index’, 1 或 ‘columns’}, 默认 None 如果对齐两个不同尺寸的对象，则沿此axis广播值
'''

# df_1 = data.iloc[:6,:3] + 2
# df_2 = data.iloc[3:10,1:5]
# print('df_1:',df_1,'*'*80,sep='\n')
# print('df_2:',df_2,'*'*80,sep='\n')
# a,b = df_1.align(df_2,join='outer',axis=None)
# print('a:',a,'*'*80,sep='\n')
# print('b:',b,'*'*80,sep='\n')                     #Both:使用指定的每个轴索引的连接方法，将轴上的两个对象对齐

# exit()
# ---------------------
'''pd.all:返回是否所有元素都为真(可能在轴上),这里要注意0和空值(NaN)的区别'''
'''
axis : {0 或 ‘index’, 1 或 ‘columns’, None}, 默认 0 指出哪个轴或哪个轴应该减少。
    0 / ‘index’ : 列方向,减少索引，返回索引为原始列标签的Series。
    1 / ‘columns’ : 行方向,减少列，返回一个索引为原始索引的Series。
    None : 减少所有轴，返回一个标量。
bool_only : bool, 默认 None,只包含布尔列。如果没有，将尝试使用一切，然后只使用布尔数据。不适用于Series。
skipna : bool, 默认 True,排除NA/null值。如果整个row/column为NA，并且skipna为True，那么对于空row/column，结果将为True。如果skipna是False，那么NA就被当作True，因为它们不等于零。
level : int 或 level name, 默认 None,如果轴是一个多索引(层次结构)，则沿着特定的level进行计数，并折叠成一个Series。
**kwargs : any, 默认 None
附加关键字没有效果，但是可以接受与NumPy兼容。
'''
# data.iloc[2,2] = 0
# print(data)
# data = data.all(axis=0,skipna=False)                         #Both:判断是否所有的值都是真
# -------------------------
'''any:判断是否有真值(可能在轴上)。'''
'''
axis : {0 or ‘index’, 1 or ‘columns’, None}, 默认 0 指出哪个axis或哪个axis应该减少
    0 / ‘index’ : 减少索引，返回索引为原始列标签的Series。
    1 / ‘columns’ : 减少列，返回一个索引为原始索引的Series。
    None:减少所有轴，返回一个标量。
bool_only : bool, 默认 None,只包含布尔列。如果没有，将尝试使用一切，然后只使用布尔数据。不适用于Series。
skipna : bool, 默认 True,排除NA/null值。如果整个行/列为NA并且skipna为True，那么结果将为False，对于空行/列也是如此。如果skipna是False，那么NA就被当作True，因为它们不等于零。
level : int 或 level name, 默认 None,如果轴是一个多索引(层次结构)，则沿着特定的级别进行计数，并折叠成一个Series。
**kwargs : any, 默认 None
附加关键字没有效果，但是可以接受与NumPy兼容。
'''
# data = data.any()                         #Both:判断是否有真值
# --------------------------
'''append:在调用者的末尾追加其他行，返回一个新对象。'''
'''
other : DataFrame或Series/类似于dict的对象，或这些对象的列表要附加的数据。
ignore_index : boolean, 默认 False,如果为True，则不要使用索引标签。
verify_integrity : boolean, 默认 False,如果为True，在创建带有重复项的索引时引发ValueError。
sort : boolean, 默认 None,如果self和other的列没有对齐，则对列进行排序。默认的排序是不赞成的，并且在将来的panda版本中将更改为不排序。
显式传递sort=True以使警告和sort保持静默。
显式传递sort=False以使警告静默，而不是sort
'''

'''concat:'''

'''merge:'''
'''
left: 第一个DataFrame;
right:第二个DataFrame;
how	默认为inner，可设为inner(交集)/outer(并集)/left/right
on	根据某列(可以是1列或多列)，必须存在于两个DateFrame中（若未同时存在，则需要分别使用left_on和right_on来设置）
left_on	左连接，以DataFrame1中用作连接键的列
right_on	右连接，以DataFrame2中用作连接键的列
left_index	将DataFrame1行索引用作连接键
right_index	将DataFrame2行索引用作连接键
sort	根据连接键对合并后的数据进行排列，默认为True
suffixes	对两个数据集中出现的重复列，新数据集中加上后缀_x,_y进行区别
'''

'''join:'''

'''combine:'''
'''
other ： DataFrame,要按列合并的DataFrame。
func ： 功能,将两个系列作为输入并返回一个Series或一个标量的函数。用于逐列合并两个数据帧。
fill_value ： 标量值，默认None,在将任何列传递给合并函数之前填充NaN的值。
overwrite ： boolean，默认为True,如果为true，列自我不存在在其他将与NaN的覆盖。
'''

'''combine_first:'''

'''update:使用来自另一个 DataFrame 的非NA值进行修改，原 df 为被更新。'''

# -----------------
'''idmax/idmin: 返回最大值/最小值的行标'''
# data = data.idxmax()                      #Both:返回每一列最大值的行标
# data = data.close.idxmin()                                #最小值
# ---------------------------

'''argsort:将x中的元素从小到大排列，提取其对应的index(这个索引是0,1,2,3....)，并返回, 需要注意:数据源中不能有空值,否则返回的结果让人很迷惑'''
# data.sort_values(by='open',ascending=True,inplace=True)
# data = data[data.open.notna()]        #去除空值,这个很重要
# data.reset_index(inplace=True)
# print('datamiddle:',data,'*'*80,sep='\n')
# data = data.open.argsort()                    #Series:
# exit()
# -------------------------
'''asfreq:将TimeSeries转换为指定的频率,注意索引需要按照升序排列'''
'''
freq ： DateOffset对象或字符串
method ： {'backfill'/'bfill'，'pad'/'ffill'}，默认None,用于填充重建索引Series中的孔的方法（请注意，这不会填充已存在的NaN）：
    'pad'/'ffill'：将最后一次有效结果传播到下一个有效
    'backfill'/'bfill'：使用NEXT有效结果来填充
how ：  {‘start’, ‘end’}，默认end,仅适用于PeriodIndex，请参阅PeriodIndex.asfreq
normalize ： bool，默认为False,是否将输出索引重置为午夜
fill_value ： 标量，可选,用于缺失值的值，在上采样期间应用（请注意，这不会填充已存在的NaN）。
'''
# data = data.sort_index(ascending=True)
# data = data.asfreq(freq='10H',normalize=True)             #Both:按指定的时间频率筛选数据
# --------------------------
'''asof:从where这点开始往前找,找到第一个不是NaN的值'''
'''
通俗的说：假如我有一组数据[1,2,3,NaN,NaN,NaN]，从where这点(假设是第二个NaN)开始往前找第一个不是NaN的值,即3;
where : 日期或日期数组 
subset : 字符串或字符串列表，默认为None，如果不是None，则使用这些列进行NaN传播
'''
# data.loc["2020-08-07":"2020-08-19",'open'] = None
# print(data)
# data = data.asof(where='2020-08-13',subset=`'open')        #Both:从where这个点开始往前数，最后一个不是空值的值
# ------------------------------
'''astype:将对象转换成指定的类型'''
'''
dtype ： 数据类型或列名称 - >数据类型,使用numpy.dtype或Python类型，将整个pandas对象强制转换为相同的类型。或者，使用{col：dtype，...}，其中col是列标签，
    dtype是numpy.dtype或Python类型，用于将一个或多个DataFrame列转换为特定于列的类型。
copy ： bool，默认为True,返回副本时copy=True（设置copy=False为更改值时要非常小心 ，然后可能会传播到其他pandas对象）。
errors ： {‘raise’, ‘ignore’}，默认‘raise’,控制提供dtype的无效数据的异常。
    raise ：允许引发异常
    ignore：抑制异常。出错时返回原始对象
版本0.20.0中的新功能。

kwargs ： 传递给构造函数的关键字参数
'''
# data = data.close.astype(str)           #Both:把对象转换成指定的数据类型，数据类型种类见pandas数据类型
# ----------------------------
'''convert_dtypes:使用dtypes支持将列转换为最佳的dtypespd.NA。'''
'''
infer_objects：bool, 默认为 True,是否将对象dtypes转换为最佳类型。
convert_string：bool, 默认为 True,对象dtype是否应转换为StringDtype()。
convert_integer：bool, 默认为 True,是否(如果可能)转换为整数扩展类型。
convert_boolean：bool, defaults True,对象dtype是否应转换为BooleanDtypes()。
'''
# data = data.convert_dtypes()              #Both:pandas1.0以上才支持
# --------------------------------------------------
'''at_time:在特定时间选择值,（例如，上午9:30）,只针对时间,不针对日期,index必须是datetime'''
'''
time ： datetime.time或string
axis ： {0或'index'，1或'columns'}，默认为0
'''
# data = data.at_time(time='19:00:00',axis=0)              #Both:选取指定时间点的值
# ---------------------------
'''between_time:选择一天中特定时间之间的值（例如，上午9：00-9：30）。index必须是datetime,对比truncate'''
'''
start_time ： datetime.time或string
end_time ： datetime.time或string
include_start ： boolean，默认为True
include_end ： boolean，默认为True
axis ： {0或'index'，1或'columns'}，默认为0
'''
# data = data.between_time('00:30','01:00') #Both:选择一天中特定时间之间的值(例如9：00-9：30 AM)
# -------------------------
'''between:用于系列检查哪个值在第一个和第二个参数之间,返回布尔值'''
'''
left:定义左边界的标量值
right:定义右边界的标量值
inclusive:一个布尔值，默认为True。如果为False，则在检查时将排除两个传递的参数。
'''
# data = data.close.between(7,8,inclusive=True)   #Series:检查哪些值是在上下限之间，返回bool值
# ------------------------
'''clip:数据修剪,如有一组数据[7.10,7.98,6.52,8.30],上下限为7.00~8.00,修建后为[7.10,7.98,7.00,8.00];即比7小的取7,比8大的取8'''
'''
lower: 上限
upper:下限
axis:0/1
'''
# data = data.clip(7.60,8,axis=0)            #Both:给区域的值设置上下限，超出部分将被修剪
# ---------------------------------------------
'''copy:复制'''
'''
deep： bool，默认为True。创建深层副本，包括数据和索引的副本。随着deep=False无论是指数还是数据复制。
    deep = True: 深copy,源数据更改时,副本不变;
    deep = False: 浅copy,源数据更改时,副本也会被更新;
'''
# data1 = data.copy(deep=False)                         #Both:复制对象，浅拷贝和深拷贝;注如果只复制data的部分内容,貌似都是深copy;
# data.loc['2020-07-30','close'] = 100
# data2 = data.copy(deep=True)
# data.loc['2020-07-30','close'] = 100
# print("data1:",data1,sep='\n')
# print("data2:",data1,sep='\n')
# --------------------------
'''corr:计算DataFrame列之间的相关系数'''
'''
检查两个变量之间变化趋势的方向以及程度，值范围-1到+1，0表示两个变量不相关，正值表示正相关，负值表示负相关，值越大相关性越强。
'''
# data = data.close.corr(data.open)                        #Both:两列数据的相关性，见数学模型
# data = data.corr()
# data = data[data>0.95].fillna('')
# -----------------------------------
'''count:返回各列中非空数据的个数'''
# data = data.count()                       #Both:返回各列中非空数据的个数
# ----------------------------
'''cummax:累积最大值'''
'''
累积最大值：一列数据从上往下一行一行的比较，如果该行的值比前面的最大值小，该行的值被换成前面的最大值，如果该行的值大于前面的最大值则取该行的值；
axis : {0 或 ‘index’, 1 或 ‘columns’}, 默认 0,索引或轴的名称。0等于None或' index '。
skipna : boolean, 默认 True,排除NA/null值。如果整个行/列是NA，那么结果将是NA。
'''
# data = data.cummax(axis=0,skipna=True)                #Both:累积最大值
# ----------------------
'''cummin:累积最小值'''
# data = data.cummin()                      #Both:累积最小值
# -------------------------
'''cumprod:累积乘积,按照轴的方向,累积乘积'''
# data = data.cumprod(axis=0)               #Both:累积乘积
# ---------------------------
'''cumsum:累积求和'''
# data = data.append(pd.DataFrame(columns=data.columns,index=['sum']).fillna(0),sort=True)
# data = data.cumsum()                      #Both:累积求和
# -------------------
'''describe:'''
'''
percentiles ： 列表类似数字，可选,要包含在输出中的百分位数。全部应该介于0和1之间。
    默认值为 ，返回第25，第50和第75百分位数。[.25, .5, .75]
include ： 'all'，类似于dtypes或None（默认值），可选,要包含在结果中的数据类型的白名单。被忽略了Series。
    以下是选项：
    'all'：输入的所有列都将包含在输出中。类似于dtypes的列表：将结果限制为提供的数据类型。将结果限制为数字类型提交numpy.number。
            要将其限制为对象列，请提交numpy.object数据类型。
            字符串也可以以select_dtypes,（例如df.describe(include=['O'])）的方式使用。要选择pandas分类列，请使用'category'
    None (default) ：结果将包括所有数字列。
exclude ： 类似于dtypes或None（默认值），可选，要从结果中省略的黑色数据类型列表。被忽略了Series。
    以下是选项：
    类似于dtypes的列表：从结果中排除提供的数据类型。
    要排除数字类型提交numpy.number。要排除对象列，
    请提交数据类型numpy.object。字符串也可以以select_dtypes
    （例如df.describe(include=['O'])）的方式使用。
    要排除pandas分类列，请使用'category'
    None (default)：结果将不包含任何内容。
'''
# data = data.describe(percentiles=[0.25,.5,.75])                    #Both:生成描述性统计数据，总结数据集分布的集中趋势
# ---------------------------
'''diff:对同一列数据进行错位相减'''
'''
periods：移动的幅度，int类型，默认值为1。
axis：移动的方向，{0 or ‘index’, 1 or ‘columns’}，如果为0或者’index’，则上下移动，如果为1或者’columns’，则左右移动。
'''
# data = data.diff(periods=1,axis=0)         #Both:对同一列数据进行错位相减
# ------------------------------------
'''div:获取数dataframe和其他元素的浮点除法'''
'''
other ： 标量 (scalar)，序列(sequence)，Series或DataFrame,任何单个或多个元素数据结构或类似列表的对象。
    other=scalar: 每一个值都会除以该标量;
    other=[10,5,6,7,2]: 列表里值的个数需要和列的个数对应,每一列除以对应的值;
axis ： {0 或 ‘index’, 1 或 ‘columns’},是否通过索引 (0 or ‘index’) 或列(1 或 ‘columns’)进行比较。对于Series输入，轴匹配Series索引。
level ： int或label,跨级别广播，匹配传递的MultiIndex级别的索引值。
fill_value ： float或None，默认为None,在计算之前使用此值填充现有缺失（NaN）,值以及成功DataFrame对齐所需的任何新元素。
如果缺少相应DataFrame位置中的数据，则结果将丢失。
'''
# data = data.div([10,5,6,7])                 #Both:获取数dataframe和其他元素的浮点除法，每一个元素除以给的参数
# -----------------------------------------
'''rdiv:反向除法，用给的参数除以每一个元素,用法同div'''
# data = data.rdiv([100,200,300,160,10])                #Both:反向除法，用给的参数除以每一个元素
# ---------------------------------
'''divide: dataframe/other在灵活的包装器（add，sub，mul，div，mod，pow）中算术运算符：+，-，*，/，//，％，**。'''
'''
other ： 标量 (scalar)，序列(sequence)，Series或DataFrame,任何单个或多个元素数据结构或类似列表的对象。
axis ： {0 或 ‘index’, 1 或 ‘columns’},是否通过索引 (0 or ‘index’) 或列(1 或 ‘columns’)进行比较。对于Series输入，轴匹配Series索引。
level ： int或label,跨级别广播，匹配传递的MultiIndex级别的索引值。
fill_value ： float或None，默认为None,在计算之前使用此值填充现有缺失（NaN）,值以及成功DataFrame对齐所需的任何新元素。
'''
# data = data.close.divide(10)              #Both:获取数据帧和其他元素的浮动除法
# ---------------------------------
'''dot:计算DataFrame与其他之间的矩阵乘法。'''
'''
other ： Series，DataFrame或类似数组,用于计算矩阵乘积的另一个对象。
'''
# df_1 = data.iloc[15:18,:3].values
# df_2 = data.iloc[16:19,:3].values
# print(df_1)
# print(df_2)
# data = df_1.dot(df_2)                       #Both:矩阵乘积
# -------------------------------------------
'''duplicated:重复数据判断'''
'''
subset：用于识别重复的列标签或列标签序列，默认所有列标签
keep=‘frist'：除了第一次出现外，其余相同的被标记为重复
keep='last'：除了最后一次出现外，其余相同的被标记为重复
keep=False：所有相同的都被标记为重复
'''
# data = data.duplicated(subset=['high'],keep=False)                #Both:重复数据判断
# data = data[data.duplicated(subset=['high'],keep=False)]
# ----------------------------
'''filter:根据指定的标签,提取对应的行或者列'''




# -----------------------------------------------
'''first:返回前几天日历日的数据,需要升序排列才有效'''
# data = data.first('10D')                   #Both:返回前几天日历日的数据
# ----------------------------
'''last:返回后几天日历日的数据,需要升序排列才有效'''
# data = data.last('10D')                   #Both:获取最后10天（日历天）的数据，而不是最后10行的数据，注意日期需要升序排列，
# ------------------------------------------
'''first_valid_index:从上往下找,第一个不是空的值的行索引'''
# data = data.close.first_valid_index()      ##Both:找到第一个不是空值的行标
# ----------------------------
'''last_valid_index:从上往下找,最后一个不是空的值的行索引'''
# data = data.last_valid_index()        #Both:找到最后一个不是空值的行标

'''floordiv:整数除法,省略了小数点'''
'''
other:序列或标量值
    other=scalar
    other = [2,2,3,4,6],个数和列对应
fill_value:在计算之前，请使用此值填充现有的缺失(NaN)值以及成功进行系列比对所需的任何新元素。
level:在一个级别上广播，在传递的MultiIndex级别上匹配索引值
'''
# data = data.floordiv(other=[2,2,4,2,2])             #Both:返回数据的整数除法
# data = data / 2                             #除法,等效data.div(2)
# data = data.div(2)
# ----------------------------
'''str:series的str API'''
# data = data.open.astype(str).str.split('.')    #seriess:字符串方法应用于每一个元素
# ----------------------
'''str.get():通过元素中的位置获取元素中的子元素'''
'''
i:要提取的元素的位置，仅整数值。
'''
# data = data.close.astype(str).str.get(i=2)  #Series:通过元素中的位置获取元素中的子元素
# -------------------------
'''groupby:按xx分组，然后配合各种数学函数std,mean,median,max,min,sum,count等使用'''
'''
方法总结
•首先通过groupby得到DataFrameGroupBy对象, 比如data.groupby('race') 
•然后选择需要研究的列, 比如['age'], 这样我们就得到了一个SeriesGroupby, 它代表每一个组都有一个Series 
•对SeriesGroupby进行操作, 比如.mean(), 相当于对每个组的Series求均值
注: 如果不选列, 那么第三步的操作会遍历所有列, pandas会对能成功操作的列进行操作, 最后返回的一个由操作成功的列组成的DataFrame
'''

# data = data.reset_index()
# data['Note'] = data.apply(lambda x: 'AA' if x.close>8 else('BB' if 7.5<x.close<7.9 else "CC"),axis=1)  #lambda 多条件判断
# data = data.groupby('Note')                     #得到DataFrameGroupBy 对象;就是Note下面全是'AA'的和'BB'...的DataFrame;
# a,b,c = data.groupby('Note') 
# print(a)
# print(b)
# print(type(c))
# data.groupby('Note').apply(lambda x: print(x))      #apply每次传入一个DataFrame;
# ---------------------------------------------------------------------------------------------------
# def plot_show(x):
    # x.boxplot(column='open',by='trade_date')
    # plt.show()
# data.groupby('Note').apply(plot_show)      #这样就可以两次分组然后图示化
# ---------------------------------------------------------------------------------------------------

# data.groupby('Note').agg(lambda x: print(x,'*'*50,sep='\n'))      #agg每次只传入一个DataFrame的一列,顺序为 A:'open',B:'open',C:'open',A:'close',B:'close'....
# data = data.groupby('Note').agg([max,min,'mean',sum,'median','std','var','count'])      #agg可以同时传入多个函数,是不是很棒
# data = data.groupby('Note').agg({'open':max,'close':[sum,min,'median'],'high':['mean','std'],'low':['var','count']})  #对不同的列求不同的值
# data['avg_open'] = data.groupby('Note')['open'].transform('mean')   #每一组指定的列的平均值, 注意transform()与apply的区别

# data['TF'] = data.apply(lambda x: 'T' if (x.close-x.open)>0 else 'F',axis=1)
# data = data.groupby('Note')['TF'].value_counts().unstack()
# exit()
# data = data.groupby('Note')['open'].sum()       #group之后取对应的列进行函数应用,如果不指定列,默认对所有列进行函数应用;
# -------------------------
'''head:取头部'''
# data = data.head(n=7)                       #Both:查看数据的前n行，默认5行，只有一个参数n
# -----------------------
'''tial:取尾部'''
# data = data.tail(n=7)                       #Both:查看数据的最后n行，默认5行，只有一个参数n
# ---------------------------
'''infer_objects:用于将具有对象数据类型的DataFrame的列转换为更具体的类型(dtypes)'''
# data.loc['2020-08-14','high'] = 'A'        #在high列放一个字符串,这样该列就变成了object类型;
# data = data.query("high != 'A'")          #将high列的'A'值剔除掉后,high列还是object类型
# data = data.infer_objects()              #适用infer_objects()函数后,high列变成了float类型
# ---------------------------------------
'''info:打印DataFrame的简要摘要,'''
'''
verbose ： bool，可选,是否打印完整的摘要。默认情况下，pandas.options.display.max_info_columns遵循中的设置 。
buf ： 可写缓冲区，默认为sys.stdout,将输出发送到哪里。默认情况下，输出将打印到sys.stdout。如果需要进一步处理输出，请传递可写缓冲区。
max_cols ： int，可选,何时从详细输出切换到截断输出。如果DataFrame的列数超过max_cols列，则使用截断的输出。默认情况下，使用中的设置 pandas.options.display.max_info_columns。
memory_usage ： bool，str，可选,指定是否应显示DataFrame元素（包括索引）的总内存使用情况。默认情况下，这遵循pandas.options.display.memory_usage设置。True始终显示内存使用情况。False永远不会显示内存使用情况。
‘deep’ 的值等效于“真正的内省”。内存使用情况以可读单位（以2为基数的表示形式）显示。无需深入自省，就可以根据列dtype和行数进行内存估计，
假设值为相应的dtype消耗相同的内存量。使用深度内存自省，将以计算资源为代价执行实际内存使用量计算。
null_counts ： 布尔值，可选,是否显示非空计数。默认情况下，仅当框架小于 pandas.options.display.max_info_rows和时显示 pandas.options.display.max_info_columns。
值为True始终显示计数，而值为False则不显示计数。
'''
# data = data.info()                          #DataFrame结构基本信息,describe是内容信息
# ---------------------------------
'''inset:DataF:在指定的位置插入列'''
'''
loc:  int型，表示第几列；若在第一列插入数据，则 loc=0
column: 给插入的列取名，如 column='新的一列'
value：数字，array，series等都可（可自己尝试）
allow_duplicates: 是否允许列名重复，选择Ture表示允许新的列名与已存在的列名重复。
'''
# data.insert(loc=2,column='gap',value=data.high-data.open,allow_duplicates=True)

# --------------------------------------------
'''interpolate:向DataFrame中插入值,处理缺失值使用;请注意，只有method='linear'具有MultiIndex的DataFrame/Series支持。'''
'''
method ： str，默认为‘linear’,使用插值技术。之一：
‘linear’：忽略索引，并将值等距地对待。这是MultiIndexes支持的唯一方法。
‘time’: 处理每日和更高分辨率的数据，以内插给定的时间间隔长度。
‘index’, ‘values’: 使用索引的实际数值。
'pad'：使用现有值填写NaN。
‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’,‘spline’, ‘barycentric’, ‘polynomial’: 传递给 scipy.interpolate.interp1d。
    这些方法使用索引的数值。‘polynomial’和 ‘spline’ 都要求您还指定一个顺序（int），
    例如 ，
    df.interpolate(method='polynomial', order=5)
'krogh'，'piecewise_polynomial'，'spline'，'pchip'，'akima'：环绕类似名称的SciPy插值方法。请参阅注释。
'from_derivatives'：指 scipy.interpolate.BPoly.from_derivatives，它替换了scipy 0.18中的'piecewise_polynomial'插值方法。
0.18.1版中的新功能：添加了对 ‘akima’方法的支持。添加了插值方法 ‘from_derivatives’ ，该方法替换了SciPy 0.18中的 ‘piecewise_polynomial’；向后兼容，SciPy <0.18
axis ： {0或'index'，1或'columns'，None}，默认为None沿轴进行interpolate。
limit ： 整数，可选,要填充的连续NaN的最大数量。必须大于0。
inplace ： bool，默认为False,尽可能更新数据。
limit_direction ： {'forward'，'backward'，'both'}，默认为'forward',如果指定了限制，则将沿该方向填充连续的NaN。
limit_area ： {None, ‘inside’, ‘outside’}, 默认为None,如果指定了限制，则连续的NaN将填充此限制。
None：无填充限制。
‘inside’：仅填充有效值（interpolate）包围的NaN。
‘outside’: 仅在有效值之外（extrapolate）填充NaN。0.23.0版中的新功能。
downcast ： 可选， ‘infer’  或None，默认为None,如果可能，请向下转换dtype。
**kwargs,关键字参数传递给插值函数。
'''
# print(dt3.interpolate())                  #Both:根据不同的方法插入值

# ----------------------------------

'''isin:判断series/DataF中的数据是否在给的清单中'''
'''
series中:
    •values: 一个集合或列表
DataFrame中:
    •values: 可以是可迭代对象，Series，DataFrame或者是字典
'''
# data = data.isin([7.87,8.19,7.36])        #Both:判断这些数字是否在series/DataF中，返回bool值
# -------------------------------
'''isna:判断各个元素是否为空值,返回布尔值'''
# data = data.open.isna()                         #Both:判断元素是否为空值
# -----------------------------
'''isnull:'''
# data = data.isnull()                       #Both:同isna
# -----------------------------
'''items:迭代器遍历（列名，Series）对。遍历DataFrame列，返回一个具有列名称和内容为Series的元组。'''
# data = data.items()                       #Both:对DataF/Series进行遍历
# -----------------------------
'''iteritems:将DataFrame迭代为(列名, Series)对'''
# data = data.iteritems()                   #Both:同items
# ----------------------------------
'''iterrows:将DataFrame迭代为(index, Series)对。'''
# data = data.iterrows()
# ---------------------------------------
'''itertuples(): 将DataFrame迭代为元祖。对每一行迭代'''
# data = data.itertuples()
# ----------------------------------------
'''where:将符合条件的值保留'''
'''
cond: scalar,series/DataFrame,callable,默认None,判断的条件,它会对series/DataF中的每一个值进行迭代判断;
other: scalar,series/DataFrame,callable,用于填充的值;
inplace: boolen, 默认False;
axis: 0/1, 默认None
level: int
errors:str,{'raise','ignore'}
try_cast:
'''
# data = data.where(data>8,other='')       #Both:将复合条件的值保留，其他值用other值替换，与mask相反
# ------------------------------------
'''mask:将符合条件的给屏蔽掉'''
# data = data.mask(data>8,other=100)        #Both:将复合条件值用other值替换，其他值保持
# -------------------------------
'''max:取最大值'''
# data = data.max()                         #Both:返回每一列的最大值
# ----------------------------------
'''min:取最小值'''
# data = data.min()                         #Both:返回每一列的最小值
# --------------------------
'''mean:平均值'''
# data = data.mean()                        #Both:返回每一列的平均值
# -------------------------------
'''median:中间值'''
# data = data.median()                      #Both:返回每一列的中间值
# ------------------------
'''sum:'''
# data = data.sum()

'''quantile():
q : 数字或者是类列表，范围只能在0-1之间，默认是0.5，即中位数-第2四分位数
axis :计算方向，可以是 {0, 1, ‘index’, ‘columns’}中之一，默认为 0
interpolation（插值方法）:可以是 {‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}之一，默认是linear。
'''
# data = data.quantile(q=0.25,axis=0)



'''memory_usage:'''
# data = data.memory_usage()                #Both:返回每一列内存使用情况
# --------------------------
'''mode:获取沿选定轴的每个元素的mode(s),出现次数最多的'''
'''
axis : {0 或 ‘index’, 1 或 ‘columns’}, 默认为0,搜索mode时要迭代的axis：
    1) 0或'index'：获取各列的mode
    2) 1或'columns'：获取每一行的mode。
numeric_only ： bool，默认为False,如果为True，则仅适用于数字列。
dropna ：bool，默认为True,不要考虑NaN / NaT的计数。
'''
# data = data.mode(axis=0,dropna=True)                  #Both:获取众数，可选选择行或列, 如果出现2个以上的,说明他们是并列的
# -------------------------------
'''mul:等价于dataframe * other，但是支持用fill_value替换其中一个输入中丢失的数据。与反向版本，rmul。'''
'''
other : scalar, sequence, Series, 或 DataFrame,何单个或多个元素数据结构，或类似列表的对象。
axis ：{0 或 ‘index’, 1 或 ‘columns’},是按索引(0或' index ')还是按列(1或' columns ')进行比较。对于Series输入，轴上匹配Series索引。
level ：int 或 label,跨级别广播，匹配传递的多索引级别上的索引值。
fill_value ： float 或 None, 默认 None,在计算之前，用这个值填充现有的缺失值(NaN)和成功的DataFrame对齐所需的任何新元素。
如果两个对应的DataFrame位置中的数据都丢失了，那么结果也将丢失。
'''
# data = data.mul(other=100,fill_value=0)         #Both:获取DataF与other的乘法值，空值用fill_value填充
# data = data.multiply(other=100,fill_value=0)   #Both:同mul
# --------------------------------------
'''nlargest:返回按列降序排列的前n行。'''
'''
n : int,要返回的行数。
columns ：标签或标签列表,要排序的列标签。
keep ：{'first'，'last'，'all'}，默认为'first',其中有重复的值:
    1) first：优先处理第一次出现的事件
    2) last：确定最后出现的优先顺序
    3) all: 请勿丢弃任何重复项，即使这意味着
选择n个以上的项目。
'''
# data = data.close.nlargest(3)             #Series:获取最大的前3个
# data = data.nlargest(3,'close')           #DataF:获取最大的前3个
# -------------------
'''nsmallest:返回按列升序排列最小的前n行。'''
'''
n ： int,要检索的项目数。
columns ：list 或 str,列名或按顺序排列的名称。
keep ： {‘first’, ‘last’, ‘all’}, 默认 ‘first’,其中有重复的值:
    1) first : 以第一个事件为例。
    2) last : 以最后一个事件为例。
    3) all : 不要删除任何重复项，
即使这意味着要选择超过n个项目。
'''
# data = data.close.nsmallest(3)            #Both:获取最小的前3个
# data = data.nsmallest(5,'close')
# ----------------------------
'''notna:'''
# data = data.notna()                        #Both:返回布尔值，判断是否为空值, 与isna相反
# ------------------------
'''notnull:'''
# data = data.notnull()                     #Both:同notna
# ----------------------------
'''unique:返回series中的唯一值'''
# data = data.close.unique()                #Series:返回series中的唯一值
# ----------------------------------
'''nunique:返回series中的唯一值个数'''
'''
axis ： {0 or ‘index’, 1 or ‘columns’}, 默认为 0,要使用的轴。行为0或'index'，列为1或'columns'。
dropna ：bool, 默认为True,不要在计数中包括NaN。
'''
# data = data.nunique()               #Both:返回唯一值的数量
# -----------------------
'''pct_change:计算当前元素与先前元素之间的百分比变化。默认情况下，此函数计算前一行的百分比变化。'''
'''
periods ：int, 默认为 1,形成百分比变化所需的时间。
fill_method ：str, 默认为‘pad’,如何在计算百分比更改之前处理NAs
limit ：int, 默认为 None,停止前要填充的连续NAs的数量。
freq ：DateOffset, timedelta, 或 str（可选）
时间序列API开始使用的增量（例如,"M"或BDay()）。
'''
# data = data.pct_change(periods=2)                  #Both:计算当前元素与先前元素之间的百分比
# -------------------------------
'''prod:返回所请求轴的值的乘积。'''
'''
axis : {index (0), columns (1)},要应用的功能的轴。
skipna : bool，默认为True,计算结果时排除NA/null值。
level : int 或 level 名字, 默认为 None,如果轴是MultiIndex（分层），则沿特定级别计数，并折叠为Series。
numeric_only :bool，默认值None,仅包括float，int，boolean列。如果为None，将尝试使用所有内容，然后仅使用数字数据。未针对Series实现。
min_count : int，默认为0,执行操作所需的有效值数量。如果少于 min_count非NA值，则结果将为NA。
0.22.0版中的新增功能：添加了默认值0。这意味着全NA或空Series的总和为0，全NA或空Series 的乘积为1。
'''
# data = data.prod(skipna=True,numeric_only=True)                        #Both:返回所请求轴的值的乘积
# -------------------
'''query:使用布尔表达式查询DataFrame的列。'''
'''
expr：str,要评估的查询字符串。您可以在环境中引用变量，方法是在变量前加上'@'字符，
例如 。@a + b
您可以通过在反引号中将空格或运算符括起来来引用它们。这样，您还可以转义以数字开头或Python关键字的名称。基本上是无效的Python标识符。
有关更多详细信息，请参见注释。
例如，如果你的一列叫做a a ，
你想把它和b相加，你的查询应该是' a a ' + b。
inplace：bool,查询是应该修改数据还是返回修改后的副本

'''
# data = data.query('close>8&open<8')          #
# data = data[(data.close>8) & (data.open<8)]        #等价上一行

# # @用法:
# closemean = data['close'].mean()
# data.query("close>@closemean",inplace=True)       #当引用变量时前面加@

# -----------------------
'''rank:该方法用来排名（名次值从1开始），它可以根据某种规则破坏平级关系，'''
'''
axis:{0 or 'index',1 or 'columns'} default 0,即默认按沿着index方向排名
method:{'average','min','max','first','dense'},指定排名时用于破坏平级关系的method选项（注：值相同的位同一个分组）
method 说明
    'average' 默认：在相等分组中，为各个值分配平均排名 
    'min' 使用整个整个分组的最小排名 
    'max' 使用整个分组的最大排名 
    'first' 按值在原始数据中的出现顺序分配排名 
    'dense' 与'min'类似，但是排名每次只会增加1，即并列的数据只占据一个名次 
ascending:是否为升序，默认为True, 这是对索引排序
na_option:用于处理NaN值
na_option说明
    'keep' leave NA values where they are (defaults)
    'top' smallest rank if ascending 
    'bottom' smallest rank if dscending 
5. pct名次是否为百分数 
'''
# data = data.rank(axis=0,method='max',ascending=True,na_option='bottom',pct=True)                  #Both:返回元素的名次
# -----------------------
'''set_index:使用现有列设置DataFrame索引'''
'''
keys：label 或 array-like 或 list of labels/arrays,此参数可以是单个列键，长度与调用DataFrame相同的单个数组，也可以是包含列键和数组的任意组合的列表。在这里，“array”包含Series，Index，np.ndarray和Iterator。
drop：bool, 默认为 True,删除要用作新索引的列。
append：bool, 默认为 False,是否将列追加到现有索引。
inplace：bool, 默认为 False,修改DataFrame到位(不要创建新对象)。
verify_integrity：bool, 默认为 False,检查新索引是否重复。否则，将检查推迟到必要时进行。设置为False将提高此方法的性能。
'''
# data.set_index('close',drop=True,append=False,inplace=True)            #将 DataFrame 中的列转化为行索引

# 追加成多级索引
# data['note'] = data.apply(lambda x: 'AA' if x.close>8 else 'BB',axis=1)
# data.set_index(keys=['note'],inplace=True,append=True)
# data = data.swaplevel('note','trade_date')

# -----------------------
'''reset_index:重置数据帧的索引，并使用默认索引。如果数据帧具有多重索引，则此方法可以删除一个或多个level'''
'''
level：可以是int, str, tuple, or list, default None等类型。作用是只从索引中删除给定级别。默认情况下删除所有级别。
drop：bool, default False。是否将原索引还原成列。
inplace：bool, default False。是否要原地修改数据。
col_level：int or str, default=0。如果列有多个级别，则确定将标签插入到哪个级别。默认情况下，它将插入到第一层。
col_fill：object, default。如果列有多个级别，则确定其他级别的命名方式。如果没有，则复制索引名称。
'''
# data = data.reset_index(drop=True)        #可以还原索引，重新变为默认的整型索引,设置为默认的行索引
# ----------------------------
'''reindex:自定义索引标签'''
'''
labels:新标签/索引使“ axis”指定的轴与之一致。
index: 指定行标签索引,
columns:指定列标签索引。最好是一个Index对象，以避免重复数据
axis:轴到目标。可以是轴名称(“索引”，“列”)或数字(0、1)。如果指定了axis,新的索引[x,y,...]就不能指定是给index还是columns;
method:{None，“ backfill” /“ bfill”，“ pad” /“ ffill”，“ nearest”}，可选,给定的索引值与原索引值不同时会显示空值,method就是填充方法;
copy:即使传递的索引相同，也返回一个新对象
level:在一个级别上广播，在传递的MultiIndex级别上匹配索引值
fill_value:在计算之前，请使用此值填充现有的缺失(NaN)值以及成功完成DataFrame对齐所需的任何新元素。如果两个对应的DataFrame位置中的数据均丢失，则结果将丢失。
limit:向前或向后填充的最大连续元素数
tolerance:不完全匹配的原始标签和新标签之间的最大距离。匹配位置处的索引值最满足方程abs(index [indexer]-target)
keywords for axes:array-like, optional
New labels / index to conform to, should be specified using keywords. Preferably an Index object to avoid duplicating data.
method:{None, ‘backfill’/’bfill’, ‘pad’/’ffill’, ‘nearest’}
    Method to use for filling holes in reindexed DataFrame. Please note: this is only applicable to DataFrames/Series with a monotonically increasing/decreasing index.
        •None (default): don’t fill gaps
        •pad / ffill: 向前填充 Propagate last valid observation forward to next valid.
        •backfill / bfill: 向后填充Use next valid observation to fill gap.
        •nearest: Use nearest valid observations to fill gap.
copy:bool, default True,Return a new object, even if the passed indexes are the same.
level:int or name,Broadcast across a level, matching Index values on the passed MultiIndex level.
fill_value:scalar, default np.NaN,Value to use for missing values. Defaults to NaN, but can be any “compatible” value.
limit:int, default None,Maximum number of consecutive elements to forward or backward fill.
tolerance:optional,Maximum distance between original and new labels for inexact matches. The values of the index at the matching locations most satisfy the equation abs(index[indexer] - target) <= tolerance.
Tolerance may be a scalar value, which applies the same tolerance to all values, or list-like, which applies variable tolerance per element. List-like includes list, tuple, array, Series, and must be the same size as the index and its dtype must exactly match the index’s type.
'''

# data = data.reindex(labels=pd.to_datetime(['2020-08-12','2020-08-15','2020-08-17']),    # 在判断所给的索引是否和原索引一致时,包括内容和格式;
                    # # index=['2020-08-04','2020-08-05','2020-08-06'],
                    # # columns=['open','a','close','d'],
                    # axis=0,            #不能和index和columns同时使用
                    # method=None,
                    # copy=True,
                    # fill_value=100,
                    # )  #重新定义行标，新行标和旧行标不一致的就是空值
# data = data.reindex(columns=sorted(data.columns))     #重新定义列标
# data.index = [1,2,3,.....]                  #也可以直接给index赋值；
# data.columns = ['a','b','c','d']
# ---------------------------
'''set_axis:用新索引替换旧索引; 用于将所需的索引分配给给定轴。可以通过分配list-like或索引来更改列标签或行标签的索引。'''
'''
labels:新索引的值。
axis:要更新的轴。值0标识行，值1标识列。
inplace:是否返回新的％(klass)s实例
'''
# didx = pd.date_range(start ='2014-08-10 10:00', freq ='D',  
                     # periods = data.shape[0], tz = 'Asia/Hong_Kong')
# data.set_axis(didx,axis=0,inplace=True)

# idx = pd.Index(['a','b','c','e','f'])
# data.set_axis(idx,axis=1,inplace=True)

# lt = ['a','b','c','e']
# data.set_axis(lt,inplace=True,axis=1)
# --------------------------------------------
'''reindex_like:借用另一个DataFrame的索引'''
'''
other：相同数据类型的Object,它的行和列索引用于定义此对象的新索引。
method：{None, ‘backfill’/’bfill’, ‘pad’/’ffill’, ‘nearest’}
    用于填充重新索引的数据格式中的漏洞。请注意:这只适用于索引为单调递增/递减的DataFrames/Series。
    1）None (default): 不填补空白。
    2）pad / ffill: 将上一个有效观察值传播到下一个有效观察值。
    3）backfill / bfill: 使用下一个有效观察值来填补空白。
    4）nearest: 使用最近的有效观测值来填补空白。
copy：bool，默认为True,即使传递的索引相同，也返回一个新对象。
limit：int, 默认为 None,填写不完全匹配的连续标签的最大数量。
tolerance：可选,最大距离之间的原始和新标签不准确的匹配。匹配位置的索引值最满足等式
abs(index[indexer] - target) <= tolerance。tolerance可以是标量值，它对所有值应用相同的tolerance，也可以是类似于列表的值，它对每个元素应用可变tolerance。类列表包括列表、元组、数组、序列，并且必须与索引大小相同，
其dtype必须与索引的类型完全匹配。
'''
# data2 = data.head()
# data = data.reindex_like(data2)       #引用data2的索引
# -------------------------
'''rename:给索引改名字'''
'''
mapper: 类似字典或函数,类似Dict或函数的转换，以应用于该轴的值。二者必选其一mapper，并axis与指定轴的目标mapper，或index和 columns。
index: 类似字典或函数,指定axis (mapper, axis=0相当于index=mapper)的替代方法。
columns: 类似字典或函数,指定axis (mapper, axis=1等同于columns=mapper)的替代方法。
axis:int 或 str,轴到目标与mapper。可以是轴名(' index '， ' columns ')或数字(0,1)，默认为' index '。
copy:bool, 默认 True,还要复制底层数据。
inplace:bool, 默认为 False,是否返回一个新的DataFrame。如果为真，则忽略copy的值。
level:int 或 level name, 默认 None,对于多索引，只能在指定的级别重命名标签。
errors:{‘ignore’, ‘raise’}, 默认 ‘ignore’,如果‘raise’，则在类似于dict的映射器、索引或列包含正在转换的索引中不存在的标签时引发键错误。如果 ‘ignore’,现有的键将被重命名，
额外的键将被忽略。
'''
# data = data.rename(columns={'open':'Open','high':'High'})  #给索引改名字
# data = data.rename(index={pd.to_datetime("2020-08-04"):'a',datetime.datetime.strptime("2020-08-17",'%Y-%m-%d'):'b'})
# data = data.rename(str.upper, axis='columns')    #把列的字体改成大写
# -------------------------------------
'''rename_axis:设置索引或列的axis名称。'''
'''
mapper : scalar, 类似list, optional,设置axis名称属性的值。
index, columns : scalar, 类似list, 类似dict 或 function, 可选,标量，类似于列表，类似于dict或函数的转换，以应用于该axis的值。使用mapper和axis，可以使用mapper或index 和/或columns指定要指定的轴。在版本0.24.0中更改。
axis : {0 或 ‘index’, 1 或 ‘columns’}, 默认为 0,重命名的轴。
copy : bool, 默认 True,还要复制底层数据。
inplace : bool, 默认为 False,直接修改对象，而不是创建新的Series或DataFrame。
'''
# data.rename_axis('Date',inplace=True)       #对更改轴的名称
# data.rename_axis('trade',axis='columns',inplace=True)       #更改轴的名称
# ----------------------------------------------
'''sort_index:对索引进行排序'''
'''
Sort object by labels (along an axis).
Returns a new DataFrame sorted by label if inplace argument is False, otherwise updates the original DataFrame and returns None.

Parameters
axis:       {0 or ‘index’, 1 or ‘columns’}, default 0
            The axis along which to sort. The value 0 identifies the rows, and 1 identifies the columns.
level:      int or level name or list of ints or list of level names
            If not None, sort on values in specified index level(s).
ascending:  bool or list of bools, default True
            Sort ascending vs. descending. When the index is a MultiIndex the sort direction can be controlled for each level individually.
inplace:    bool, default False
            If True, perform operation in-place.
kind:       {‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’
            Choice of sorting algorithm. See also ndarray.np.sort for more information. mergesort is the only stable algorithm. For DataFrames, this option is only applied when sorting on a single column or label.
na_position:    {‘first’, ‘last’}, default ‘last’
                Puts NaNs at the beginning if first; last puts NaNs at the end. Not implemented for MultiIndex.
sort_remaining: bool, default True
                If True and sorting by level and index is multilevel, sort by other levels too (in order) after sorting by specified level.
ignore_index:   bool, default False
                If True, the resulting axis will be labeled 0, 1, …, n - 1.
'''
# data.sort_index(axis=1,ascending=True,inplace=True)          #对索引进行排序，axis: 0 行，1列；
# ---------------------------------------------
'''重新排列列的顺序,这是个苯方法'''
# ord = list(data)                #将列标签转成列表;
# ord.sort()                      #对列标签的列标进行排序;
# data = data.loc[:,ord]          #将列重新排列，包括列标和内容；
# data[['open','close','low','high','pct_chg']] = data[['high','close','low','open','pct_chg']]   #将列的内容重新排列，但是列标签不变

# ----------------------------------------
'''sort_values:对行或者列进行排序'''
'''
by:         指定列名(axis=0或'index')或索引值(axis=1或'columns') 
axis:       若axis=0或'index'，则按照指定列中数据大小排序；若axis=1或'columns'，则按照指定索引中数据大小排序，默认axis=0 
ascending:  是否按指定列的数组升序排列，默认为True，即升序排列 
inplace:    是否用排序后的数据集替换原来的数据，默认为False，即不替换 
na_position:    {‘first',‘last'}，设定缺失值的显示位置 
'''
# data.sort_values(by='open',inplace=True)                  #对列值进行排序
# ---------------------------------------------
'''repeat:每个元素的重复次数'''
'''
repeats:每个元素的重复次数。
'''
# data = data.high.repeat(repeats=3)        #series: 将没一个元素重复指定的次数；
# --------------------------------
'''replace: 前面是需要被替换的值，后者是替换后的值'''
'''
to_replace：
    str，
    regex，
    list，
    dict，
    Series，
    int，
    float
    或None，将被替换的值；
value：标量，字典，列表，str，正则表达式，要替换的值；
inplace：True就地修改；
limit：int，限制向前或向后填充的数量；
regex：bool或与to_replace相同的类型;正则表达式；
method： {‘pad’, ‘ffill’,‘backfill’, ‘bfill’, None}；
    pad/ffill：用前一个非缺失值去填充该缺失值； 
    backfill/bfill：用下一个非缺失值填充该缺失值;
    None：指定一个值去替换缺失值（缺省默认这种方式）
 '''
# 选取替换区域,这个区域的选取和正常的取值方法一样: 按列,按行,按区域
# data.replace(7.58,'A',inplace=True)         #查找全部，将值为7.58替换成‘A'，原地修改
# data.high.replace(to_replace=7.58,value='B',inplace=True)   #在某一列查找，如果同时在多列查找的话用inplace会报错，要用下面那种方式
# data[['close','high']].replace(to_replace=7.58,value='B',inplace=True)   #在某几列查找，返回的也只有这几列的值
# data.iloc[1:6,:].replace({7.50:100,7.80:12},inplace=True,method='bfill')

# 如果只给to_replace赋值,不给value赋值: 默认是用上一行的值来替换replace里指定的值
# data.replace(to_replace=[8.05,7.99],inplace=True)  
# data.replace(to_replace=8.05,inplace=True)

# 主要介绍 to_replace 和 value 参数类型
# int,str,flost类型:
# data.replace(to_replace=7.8,value=100,inplace=True)
# data.replace(to_replace=8.01,value='m',inplace=True)
# data.replace(to_replace='m',value='python',inplace=True)

# list类型: 既然用了list了,基本都是多个数值的替换; 注意:to_replace和value的list长度要一致,或者to_replace是list,value是str,int,float;
# data.replace(to_replace=[7.99,8.05,7.98],value=[1000,'python','dog'],inplace=True)
# data.replace([7.80,7.90,8.05],200,inplace=True)       #列表形式，把不同目标替换成同一个值

# dict类型: 如果to_replace是dict类型,value是不用传值的:
# data.replace(to_replace={7.80:'m',7.90:'n',8.05:100},inplace=True)     #字典形式

# regex类型:使用正则表达式替换，当使用正则表达式时，需要regex=True
# data.replace(to_replace=[7.99,7.98,7.53,8.04],value='python',inplace=True)
# rr = re.compile(r'\w*o\w',re.I)
# data.replace(to_replace=rr,value='regex',inplace=True,regex=True)

# str.replace: 调用str API, 这个相当于对单个字符串进行处理
# data.loc[data.high>8.00,'Note'] = 'AAB'     #将high列值大于8的添加Note备注'AAB’;
# data.loc[data.high<8.00,'Note'] = 'AAC'     #将high列值小于8的添加Note备注'AAC’;
# data = data.Note.str.replace('C','D')       #将Note列值中的'C'替换成'D'; 当使用str.replace的时候不能使用inplace;
# ------------------------------------------------
'''round:四舍五入 取小数的位数'''
# data = data.round(1)                        #四舍五入，保留指定小数位数
# ----------------------------------------------------------
'''sample:随机抽样'''
'''
n:  是要抽取的行数。（例如n=20000时，抽取其中的2W行）
frac:   是抽取的比列。（有一些时候，我们并对具体抽取的行数不关系，我们想抽取其中的百分比，这个时候就可以选择使用frac，例如frac=0.8，就是抽取其中80%）
replace：是否为有放回抽样，取replace=True时为有放回抽样。
weights:    这个是每个样本的权重，具体可以看官方文档说明。
random_state:   这个在之前的文章已经介绍过了。
axis:   是选择抽取数据的行还是列。axis=0的时是抽取行，axis=1时是抽取列（也就是说axis=1时，在列中随机抽取n列，在axis=0时，在行中随机抽取n行）
'''
# data = data.sample(frac=0.1,random_state=1)   #随机抽样
# -----------------------------------------------
'''select_dtypes: 对不同的数据类型进行取舍'''
'''
•include：要返回的列的数据类型，标量或列表
•exclude：要排除的列的数据类型，标量或列表

• To select all numeric types, use np.number or 'number'
• To select strings you must use the object dtype, but note that this will return all object dtype
columns
• See the numpy dtype hierarchy
• To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
• To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
• To select Pandas categorical dtypes, use 'category'
• To select Pandas datetimetz dtypes, use 'datetimetz'(new in 0.20.0) or 'datetime64[ns,
tz]'
'''
# data['note'] = data.apply(lambda x: 'AA' if x.open>8.1 else 'BB',axis=1)
# data = data.select_dtypes(include='object')                #筛选出数据类型为'int'的列,默认是include
# data = data.select_dtypes(exclude='float')                #可以用exclude
# -------------------------------------------
'''shift:可以把数据移动指定的位数'''
'''
period: 参数指定移动的步幅,可以为正为负.
axis:   指定移动的轴,1为行,0为列.
'''
# data = data.shift(periods=2,axis=0)                 #将数据平移，periods前后的步幅(正数或者负数)，axis(0,1)上下，还是左右(即横轴还是纵轴)
# ---------------------------------------------
'''slice_shift:功能相当于在不复制数据的情况下进行移位。移位的数据将不包括丢失的周期，并且移位的轴将小于原始数据。该功能只是沿指定方向在给定轴上放置指定的周期数。'''
'''
periods:移动的周期数，可以是正数或负数;
axis:   指定移动的轴,1为行,0为列.
'''
# data = data.slice_shift(periods=2,axis=0)           #和shift类似，只是移动后空值的行和列会被删除
# -------------------------------
'''tshift:用于移动时间索引，如果在给定的数据帧中可用，则使用索引的频率。'''
# data = data.tshift(periods=5,freq='2H')              #于移动时间索引,数值不变
# ----------------------------------
'''squeeze:将一维轴对象压缩为标量,如下例未挤之前是2020-08-07 8.33,挤之后是8.33'''
'''
axis:要挤压的特定轴。默认情况下，所有长度为1的轴都受到挤压。
'''
# data = data.open
# data = data[data == 8.33]
# data = data.squeeze()                                   #将这个值压缩成标量即：2020-07-28    7.58 压缩成 7.58
# -----------------------------
'''stack/unstack:堆叠'''
'''
说明:
    •stack：(将列标签转成行标签)“透视”某个级别的（可能是多层的）列标签，返回带有索引的 DataFrame，该索引带有一个新的最里面的行标签。
    •unstack：(将行标签转成列标签)（堆栈的逆操作）将（可能是多层的）行索引的某个级别“透视”到列轴，从而生成具有新的最里面的列标签级别的重构的 DataFrame。
    stack 过程将数据集的列转行，unstack 过程为行转列。
level ：int, str, list, 默认为 -1(最里侧的索引),从列轴堆叠到索引轴，定义为一个索引或标签，或一列索引或标签。
dropna ：bool, 默认为 True,是否删除结果Frame/Series中缺少值的行。将列级堆叠到索引轴上,可以创建原始dataframe中缺少的索引和列值的组合。
'''
# data = data.stack()                                     #堆叠，将数据的表格结构转换成花括号的层次结构，untack相反
# data = data.unstack(level=0)
# --------------------------------------
'''swapaxes:适当地交换轴和交换值轴。该功能将要交换的轴的名称作为参数。基于轴，它也会相应地更改数据。'''
'''
axis1:第一个轴的名称{字符串} 
axis2：第二个轴的名称{字符串}
'''
# data = data.swapaxes('index','columns')                 #当地交换轴和交换值轴
# data = data.T
# data = data.transpose()
# ----------------------------
'''std:标准差:
axis:{索引(0)，列(1)}
skipna:排除NA /空值。如果整个行/列均为NA，则结果为NA
level:如果轴是MultiIndex(分层)，则沿特定级别计数，并折叠为Series
ddof:Delta自由度。计算中使用的除数为N-ddof，其中N表示元素数。
numeric_only:仅包括float，int，boolean列。如果为None，将尝试使用所有内容，然后仅使用数字数据。未针对系列实施。
'''
# data = data.std(axis=0,skipna=True,numeric_only=True)




'''take:沿轴返回给定位置索引中的元素。在这里，我们不是根据对象的index属性中的实际值建立索引。我们正在根据元素在对象中的实际位置建立索引。'''
'''
indices:一个整数数组，指示要采取的位置。
axis:选择元素的轴。
    ->0表示我们正在选择行。
    ->1表示我们正在选择列。
convert:是否将负指数转换为正指数
is_copy:是否返回原始对象的副本。
'''
# data = data.take(indices=[1,3,10],axis=0)                  #沿指定的轴返回位对应位置的值
# ------------------------------
'''tolist/to_list:返回值列表。这些都是标量类型，这是Python标量(用于str，int，float)或pandas标量(用于Timestamp /Timedelta /Interval /Period)。'''
'''
没有参数
'''
# data = data.open.tolist()                               #series: 将series转换成列表
# data = data.close.to_list()
# data = data.open.values                                 #返回的是数组
# print(type(data))
# --------------------
'''value_counts:返回series中重复值的个数,DataFrame无此属性'''
'''
normalize:  bool, default False,If True then the object returned will contain the relative frequencies of the unique values.
sort:       bool, default True,Sort by frequencies.
ascending:  bool, default False,Sort in ascending order.
bins:       int, optional,Rather than count values, group them into half-open bins, a convenience for pd.cut, only works with numeric data.
dropna:     bool, default True,Don’t include counts of NaN.
'''
# data = data.low.value_counts(ascending=True,normalize=False,bins=3,dropna=False) #返回该值在列中重复的次数，normalize=True时 返回占比；
# data = data.apply(pd.value_counts)                        #对于DataFrame使用apply函数

'''truncate:在某个索引值之前和之后Truncate Series或DataFrame。'''
'''
before ：date, str, int,Truncate此索引值之前的所有行。
after ：date, str, int,Truncate此索引值之后的所有行。
axis ：{0 或‘index’, 1 或‘columns’}, 可选。Truncate轴。默认情况下Truncate索引（行）。
copy ：bool, 默认为 True
'''
# data = data.truncate(before='2020-07-30',after='2020-08-05')
# ----------------------------
'''to_frame:转换成DataFrame,Series.to_frame(self, name=None)'''
'''
name：object, 默认为 None
传递的名称应替换 Series 名称(如果有的话)。
'''
# data = pd.Series(['Jimmy','Tom','White'],name='Name')
# data = data.to_frame()


# exlude RD runs
# df = df[~df.ProductionOrder.str.startswith('9')]


print(data)
# print('index type:',data.index.dtype,sep='\n')
# print('DataFrame type:',data.dtypes,sep='\n')


'''日期格式处理'''

# date = pd.read_csv(r'.\testfile\date_sample.csv',header=0,index_col=0)      #索引和列的时间都是object格式
# print('Initial date:',date,'*'*50,sep='\n')
# print('Date types:',date.dtypes,sep='\n')
# print('Index type:',date.index.dtype,'*'*80,sep='\n')

'''Period(): 时期; 特点1: 一次只处理一个时期; 特点2: 对周期的推移处理很方便
参数:
    value: Period or compat.string_types: 时期周期,值的类型只能是Period或者各种时间字符串,如:‘4Q2005’
    freq: str, 默认None, 频率: 'Y'/'A','M'/'m','D'/'d','Q'/'q'
    
    下面这些不知怎么用??
    ordinal:
    year:
    month:
    quarter:
    day:
    hour:
    minute:
    second:
属性:
    day:
    dayofweek:
    dayofyear:
    days_in_month:
    daysinmonth:
    hour:
    minute:
    qyear:
    second:
    start_time:
    week:
    weekday:
'''

# p = pd.Period(value="4Q2005")
# p = pd.Period(value="2021-04-15 08:20:56",freq='H')
# p = pd.Period(value='2021-04-12',freq='q')
# p = pd.Period(value='20210412',freq='D')

# 有下面这些属性:
# print('P:',p, type(p))
# print('P+2:',p+2, type(p+2))
# print('p.year:',p.year, type(p.year))
# print('p.month:',p.month, type(p.month))
# print('p.day:',p.day,type(p.day))
# print('p.hour:',p.hour,type(p.hour))
# print('p.minute:',p.minute,type(p.minute))
# print('p.second:',p.second,type(p.second))
# print('p.week:',p.week,type(p.week))
# print('p.weekday:',p.weekday,type(p.weekday))
# print('p.quarter:',p.quarter,type(p.quarter))
# print('p.dayofyear:',p.dayofyear,type(p.dayofyear))
# print('p.dayofweek:',p.dayofweek,type(p.dayofweek))
# print('p.weekofyear:',p.weekofyear,type(p.weekofyear))
# print('p.is_leap_year:',p.is_leap_year,type(p.is_leap_year))

# 下列属性不适用:
# # print('p.date:',p.date)
# # print('p.normalize:',p.normalize())
# # print('p.time:',p.time)
# # print('p.weekday_name:',p.weekday_name)

# print('p type:',type(p))

'''period_range(): 返回PeriodIndex, 它是Period()的加强版,
	start： [str or period-like, default None],时期的开始点
			Left bound for generating periods.
			
	end： [str or period-like, default None], 时期的结束点
			Right bound for generating periods.
			
	periods： [int, default None], 频率
			Number of periods to generate.
			
	freq： [str or DateOffset, optional]
			Frequency alias. By default the freq is taken from start or end if those are Period objects. Otherwise, the default is "D" for daily frequency.
			
	name： [str, default None] 
			Name of the resulting PeriodIndex.
'''
# p = pd.period_range(start='20210312',
                                # # end='20210316',
                                # periods=5,
                                # freq='D',
                                # )
# 有下面这些属性:
# print('P:',p, type(p))
# print('P+2:',p+2, type(p+2))
# print('p.year:',p.year, type(p.year))
# print('p.month:',p.month, type(p.month))
# print('p.day:',p.day,type(p.day))
# print('p.hour:',p.hour,type(p.hour))
# print('p.minute:',p.minute,type(p.minute))
# print('p.second:',p.second,type(p.second))
# print('p.week:',p.week,type(p.week))
# print('p.weekday:',p.weekday,type(p.weekday))
# print('p.quarter:',p.quarter,type(p.quarter))
# print('p.dayofyear:',p.dayofyear,type(p.dayofyear))
# print('p.dayofweek:',p.dayofweek,type(p.dayofweek))
# print('p.weekofyear:',p.weekofyear,type(p.weekofyear))
# print('p.is_leap_year:',p.is_leap_year,type(p.is_leap_year))

# 下列属性不适用:
# # print('p.date:',p.date)
# # print('p.normalize:',p.normalize())
# # print('p.time:',p.time)
# # print('p.weekday_name:',p.weekday_name)
# print(type(periodrange))

'''to_period:它只吃DatetimeIndex, 返回PeriodIndex,默认接收DataFrame的Index进行处理,不能对普通的列处理; 与period的那些属性相比,to_period()增加的功能是可以将日期截取到: 年,月,日,....'''
'''
freq: str or Offset, optional; DataFrame中使用的时候,只吃DatetimeIndex,其他的都会报错
freq = "Y" : 日期取到'年'
freq = "M" : 日期取到'月'
freq = "D" : 日期取到'日'
freq = "H" : 日期取到'小时'
freq = "T" : 日期取到'分钟'
freq = "S" : 日期取到'秒'
freq = "W" : 日期是2020-08-13返回的是2020-08-10/2020-08-16; 取周需要用它的属性 .week
'''
# date.index = pd.to_datetime(date.index)
# date = date.to_period('D')      #将列索引转换成peirodindex
# date['Year'] = date.index.to_period(freq="A")   #截取到"年"
# date['Month'] = date.index.to_period(freq="M")   #截取到"月"
# date['Day'] = date.index.to_period(freq="D")   #截取到"日"
# date['Hour'] = date.index.to_period(freq="H")   #截取到"小时"
# date['Minute'] = date.index.to_period(freq="T")   #截取到"分钟"
# date['Second'] = date.index.to_period(freq="S")   #截取到"秒"
# date['Week'] = date.index.to_period(freq="D").week   #截取到"周"

# print(date)
# print(date.dtypes)
# print(date.index.dtype)
# ---------------------

'''Period.to_timestamp()
	freq:目标频率。如果self.freq为一周或更长时间，则默认为“ D”，否则为“ S”
    how:“ S”，“ E”。可以用作别名，不区分大小写：“开始”，“完成”，“开始”，“结束”

'''
# prd = pd.Period('2021-04-17',freq='D')
# tstamp = prd.to_timestamp()

# print('prd:',prd)
# print('tstamp:',tstamp)
# print(type(tstamp))

'''pd.to_datetime() 转换成Datetime格式; 可以吃各种格式, 应该是pandas里最不挑食的函数
	1. arg ：[int, ﬂoat, str, datetime, list, tuple, 1-d array, Series DataFrame/dict-like] 
	2. errors： [{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’]
		• If ‘raise’, then invalid parsing will raise an exception.
		• If ‘coerce’, then invalid parsing will be set as NaT.
		• If ‘ignore’, then invalid parsing will return the input.
	3. dayﬁrst ：[bool, default False] 
		声明传入的参数前两位是天
	4. yearﬁrst： [bool, default False] 
		声明传入的参数前两位是年
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

# date.index = pd.to_datetime(date.index)     #将索引 object-->datetime
# date['Date'] = pd.to_datetime(date.Date)    ##将Date列: object-->datetime

# DatetimeIndex的属性
# date['year'] = date.index.year
# date['month'] = date.index.month
# date['day'] = date.index.day
# date['month'] = date.index.month
# date['hour'] = date.index.hour
# date['minute'] = date.index.minute
# date['second'] = date.index.second
# date['date'] = date.index.date
# date['normalize'] = date.index.normalize()
# date['time'] = date.index.time
# date['week'] = date.index.week
# date['quarter'] = date.index.quarter
# date['weekofyear'] = date.index.weekofyear  #同week
# date['dayofyear'] = date.index.dayofyear
# date['dayofweek'] = date.index.dayofweek
# date['weekday'] = date.index.weekday
# date['weekday_name'] = date.index.weekday_name
# date['is_leap_year'] = date.index.is_leap_year

# datetime格式的列是没有上面那些属性的

# print(date)
# print(date.dtypes)
# print(date.index.dtype)

'''pd.DatetimeIndex():
Datetime格式的属性:
    date: 这个比较特殊,只吃DatetimeIndex,不吃Datetime
    day:
    dayofweek:
    dayofyear:
    days_in_month:
    daysinmonth:
    time:      这个比较特殊,只吃DatetimeIndex,不吃Datetime
    hour:
    minute:
    qyear:
    second:
    start_time:
    week:
    weekday:
'''
# 已知data.index 和data['Date'] 是object格式

# 属性见to_datetime介绍


'''date_range():  主要用来生成时间序列,DatetimeIndex
start:      str or datetime-like, optional; 开始日期;
end:        str or datetime-like, optional; 结束日期;
periods:    int,optional; 周期, 开始和结束之间取几个日期; periods,end和freq不能同时使用
freq:       str or DateOffset, default: 'D'; 有多种选择,见下面清单;
tz:         str or tzinfo, optional; 			返回本地化的DatetimeIndex的时区名，例如’Asia/Hong_Kong’
normalize:  bool, default:False; 生成日期之前,将开始/结束时间初始化为午夜;
name:       str, default:None; 生成DatetimeIndex的名字;
closed:     {None,'left','right'}, optional; 时区间相对给定频率左闭合\右闭合\双向闭合; 就是start的那一天要不要计算在内

freq 值选项: 下列值前面可以加数字,如: '3D','2M'...
    B:      business day frequency, 工作日
	C:      custom business day frequency
	D:      calendar day frequency, 日历天，也可以指定具体天数，如：5天，‘5D'；其他也是一样；
	W:      weekly frequency
	M:      month end frequency
	SM:     semi-month end frequency (15th and end of month)
	BM:     business month end frequency
	CBM:    custom business month end frequency
	MS:     month start frequency
	SMS:    semi-month start frequency (1st and 15th)
	BMS:    business month start frequency
	CBMS:   custom business month start frequency
	Q:      quarter end frequency
	BQ:     business quarter end frequency
	QS:     quarter start frequency
	BQS:    business quarter start frequency
	A, Y:   year end frequency
	BA, BY: business year end frequency
	AS, YS: year start frequency
	BAS,BYS:    business year start frequency
	BH:     business hour frequency
	H:      hourly frequency
	T, min: minutely frequency
	S:      secondly frequency
	L, ms:  milliseconds
	U, us:  microseconds
	N:      nanoseconds

'''
# daterange = pd.date_range(start='20210415', end='20210430',freq='4D',tz='Asia/Shanghai',closed=None)
# print(daterange)

'''pd.Timedelta(): 时间差
    days=0,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0
'''
# timedelta = pd.Timedelta(days=1,hours=1,minutes=1,seconds=1)
# print(timedelta)


''' timedelta_range(): 在Timedelta的基础上,生成一个timedelta序列; 逻辑和其他的 xxx_range() 一样
	start：str 或 timedelta-like, 默认为 None	左边界以生成时间增量。
	end：str 或 timedelta-like, 默认为 None	向右生成时间增量。
	periods：int, 默认为 None	要生成的周期数。
	freq：str 或 DateOffset, 默认为 ‘D’	频率字符串可以有多个，例如‘5H’。
	name：str, 默认为 None	结果TimedeltaIndex的名称。
	closed：str, 默认为 None    使间隔相对于给定的频率‘left’，‘right’或两侧(无)闭合。
'''

# td = pd.timedelta_range(start='1 days',end='3 days',freq='3H')
# print(td)

'''dt API 调用: 注意它只吃类似Datetime类型的数据, DatetimeIndex也是不可以用的'''

# date.index = pd.to_datetime(date.index)     #将索引 object-->datetime
# date['Date'] = pd.to_datetime(date.Date)    ##将Date列: object-->datetime


# date['dt_date_object'] = date['Date'].dt.date                 #返回object
# date['dt_normalize_datetime'] = date['Date'].dt.normalize()                 #返回datetime64

# dt只接收datetime格式的列,有下列属性:
# date['dt_date'] = date['Date'].dt.date
# date['normalizes'] = date['Date'].dt.normalize()
# date['dt_time'] = date['Date'].dt.time

# date['dt_year'] = date['Date'].dt.year                   
# date['dt_month'] = date['Date'].dt.month                 
# date['dt_day'] = date['Date'].dt.day
# date['dt_hour'] = date['Date'].dt.hour
# date['dt_minute'] = date['Date'].dt.minute
# date['dt_second'] = date['Date'].dt.second

# date['dt_week'] = date['Date'].dt.week
# date['dt_quarter'] = date['Date'].dt.quarter
# date['dt_weekofyear'] = date['Date'].dt.weekofyear
# date['dt_dayofyear'] = date['Date'].dt.dayofyear
# date['dt_dayofweek'] = date['Date'].dt.dayofweek
# date['dt_weekday'] = date['Date'].dt.weekday
# date['dt_weekday_name'] = date['Date'].dt.weekday_name
# date['dt_is_leap_year'] = date['Date'].dt.is_leap_year

# strftime返回的都是object
# date['str_year_object'] = date['Date'].dt.strftime('%Y')         #返回object
# date['str_month_object'] = date['Date'].dt.strftime('%Y-%m')       #返回object
# date['str_day_object'] = date['Date'].dt.strftime('%Y-%m-%d')        #返回object
# date['str_hour_object'] = date['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
# date['str_hour'] = date['Date'].dt.strftime('%H:%M:%S')
# date['str_data_str'] = date['Date'].dt.strftime('%x')            #%x返回日期字符串
# date['str_time_str'] = date['Date'].dt.strftime('%X')            #%x返回日期字符串
# date['str_week'] = date['Date'].dt.strftime('%W')

# print(date)
# print(date.dtypes)
# print(date.index.dtype)

'''timestamp(): 实际就是datetime/DatetimeIndex里的单个值, 所以它'''

# date.index = pd.to_datetime(date.index)     #将索引 object-->datetime
# date['Date'] = pd.to_datetime(date.Date)    ##将Date列: object-->datetime

# timestamp = date['Date'][0]
# print('timestamp:',timestamp)
# print('type:',type(timestamp))

# year = timestamp.year
# print('year:',year)

# month = timestamp.month
# print('month:',month)

# day = timestamp.day
# print('day:',day)

# hour = timestamp.hour
# print('hour:',hour)

# minute = timestamp.minute
# print('minute:',minute)

# second = timestamp.second
# print('second:',second)

# date = timestamp.date       #它返回的是对象的内存地址
# print(date)

# normalize = timestamp.normalize()   #返回日期和 00:00:00时间
# print(normalize)

# time = timestamp.time       #返回内存地址
# print('time:',time)

# week = timestamp.week
# print('week:',week)

# quarter = timestamp.quarter
# print('quarter:',quarter)

# weekofyear = timestamp.weekofyear   #同week
# print('weekofyear:',weekofyear)

# dayofyear = timestamp.dayofyear
# print('dayofyear:',dayofyear)

# dayofweek = timestamp.dayofweek
# print('dayofweek:',dayofweek)

# # dayweek = timestamp.dayweek     #没有此属性
# # print('dayweek:',dayweek)

# # weekday_name = timestamp.weekday_name     #没有此属性
# # print('weekday_name:',weekday_name)

# is_leap_year = timestamp.is_leap_year
# print('is_leap_year:',is_leap_year)


'''strftime():'''
# date.index = pd.to_datetime(date.index)     #将索引 object-->datetime
# date['Date'] = pd.to_datetime(date.Date)    ##将Date列: object-->datetime

# 直接接收DatetimeIndex/PeriodIndex类型数据
# date = date.to_period(freq='M')
# date['day_strfromindex'] = date.index.strftime('%x')

# 通过dt接收Datetime类型数据,返回object日期类型
# date['day_dt_strf'] = date['Date'].dt.strftime('%Y-%m-%d')

# timestamp = date['Date'][0].strftime('%X')       #接收timestamp格式
# print('timestamp_strftime:',timestamp)
# print('type_fromtimestamp:',type(timestamp))

# print(date)
# print('types:',date.dtypes)
# print('index type:',date.index.dtype)


'''asfreq(): 它会改变现有日期的频率;
freq: DateOffset or str
    Frequency DateOffset or string.
method: {‘backfill’/’bfill’, ‘pad’/’ffill’}, default None
    Method to use for filling holes in reindexed Series (note this does not fill NaNs that already were present):
    □ ‘pad’ / ‘ffill’: propagate last valid observation forward to next valid
    □ ‘backfill’ / ‘bfill’: use NEXT valid observation to fill.
how: {‘start’, ‘end’}, default end
    For PeriodIndex only (see PeriodIndex.asfreq).
normalize: bool, default False
    Whether to reset output index to midnight.
fill_value: scalar, optional
Value to use for missing values, applied during upsampling (note this does not fill NaNs that already were present).

'''

# date.index = pd.to_datetime(date.index)     #将索引 object-->datetime
# date['Date'] = pd.to_datetime(date.Date)    ##将Date列: object-->datetime

# date.sort_index(ascending=True,inplace=True)
# date = date.asfreq(freq='D',method='bfill')

'''tz_localize: 添加时区信息,输入数据类型需要时datetime格式,默认对index进行处理'''
'''
tz:字符串或pytz.timezone对象
axis:定位轴,default: 0
level:如果轴为MultiIndex，则定位特定级别。否则必须为None
copy:同时复制基础数据
ambiguous:“推断”，bool-ndarray，“ NaT”，默认为“提高”
nonexistent:str，默认为“提高”
'''
# date.index = pd.to_datetime(date.index)
# date = date.tz_localize(tz='Asia/Shanghai',axis=0)               #将tz-aware axis转换为目标时区
# ------------------------------------------
'''tz_convert(): 将带有时区信息的datetime格式时间转换成目标时区:
参数：
tz:字符串或pytz.timezone对象
axis:转换轴
level:如果轴为MultiIndex，则转换特定级别。否则必须为None
copy:同时复制基础数据
'''

# date = date.tz_convert('Europe/Stockholm')



# print(date)
# print('types:',date.dtypes)
# print('index type:',date.index.dtype)

'''multiIndex: 多级索引'''


'''to_csv:'''
'''
path_or_buf:  [str or ﬁle handle, default None] File path or object, if None is provided
            the result is returned as a string. If a ﬁle object is passed it should be opened with
            newline=”, disabling universal newlines.
            Changed in version 0.24.0: Was previously named “path” for Series.

sep:  [str, default ‘,’] String of length 1. Field delimiter for the output ﬁle.

na_rep: [str, default ‘’] Missing data representation.

ﬂoat_format [str, default None] Format string for ﬂoating point numbers.

columns:  [sequence, optional] Columns to write.

header: [bool or list of str, default True] Write out the column names. If a list of strings
        is given it is assumed to be aliases for the column names.
        Changed in version 0.24.0: Previously defaulted to False for Series.
index: [bool, default True] Write row names (index).

index_label: [str or sequence, or False, default None] Column label for index column(s)
            if desired. If None is given, and header and index are True, then the index names are
            used. A sequence should be given if the object uses MultiIndex. If False do not print
            ﬁelds for index names. Use index_label=False for easier importing in R.

mode [str] Python write mode, default ‘w’.

encoding [str, optional] A string representing the encoding to use in the output ﬁle, de-
            faults to ‘utf-8’.

compression [str or dict, default ‘infer’] If str, represents compression mode. If dict,
            value at ‘method’ is the compression mode. Compression mode may be any of the
            following possible values: {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}. If compression
            mode is ‘infer’ and path_or_buf is path-like, then detect compression mode from the
            following extensions: ‘.gz’, ‘.bz2’, ‘.zip’ or ‘.xz’. (otherwise no compression). If
            dict given and mode is ‘zip’ or inferred as ‘zip’, other entries passed as additional
            compression options.
            Changed in version 1.0.0: May now be a dict with key ‘method’ as compression mode
            and other entries as additional compression options if compression mode is ‘zip'

quoting [optional constant from csv module] Defaults to csv.QUOTE_MINIMAL.
        If you have set a ﬂoat_format then ﬂoats are converted to strings and thus
        csv.QUOTE_NONNUMERIC will treat them as non-numeric.

quotechar [str, default ‘”’] String of length 1. Character used to quote ﬁelds.

line_terminator [str, optional] The newline character or character sequence to use in the
            output ﬁle. Defaults to os.linesep, which depends on the OS in which this method is
            called (‘n’ for linux, ‘rn’ for Windows, i.e.).
            Changed in version 0.24.0.

chunksize [int or None] Rows to write at a time.

date_format [str, default None] Format string for datetime objects.

doublequote [bool, default True] Control quoting of quotechar inside a ﬁeld.

escapechar [str, default None] String of length 1. Character used to escape sep and

quotechar when appropriate.

decimal [str, default ‘.’] Character recognized as decimal separator. E.g. use ‘,’ for
        European data.


'''









































































































