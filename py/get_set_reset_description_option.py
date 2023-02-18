import pandas as pd

'''pd.set_option'''
#两种写法如:pd.options.display.max_columns = None 或 pd.set_option(display.max_columns,None)

'''
compute.use_bottleneck:bool
    Use the bottleneck library to accelerate if it is installed, the default is True Valid values: False,True [default: True] [currently: True]
compute.use_numba:bool
    Use the numba engine option for select operations if it is installed, the default is False Valid values: False,True [default: False] [currently: False]
compute.use_numexpr: bool
    Use the numexpr library to accelerate computation if it is installed, the default is True Valid values: False,True [default: True] [currently: True]
'''
'''
display.chop_threshold:float or None
    if set to a float value, all float values smaller then the given threshold will be displayed as exactly 0 by repr and friends. [default: None] [currently: None]
    设置一个阈值,小于这个值的值显示为0;
'''
# pd.options.display.chop_threshold = 11.90      #显示的阈值:T050003_Value
'''
display.colheader_justify‘left’/’right’
    Controls the justification of column headers. used by DataFrameFormatter. [default: right] [currently: right]
    列标题靠哪边对齐,默认right
'''
# pd.options.display.colheader_justify = 'left'     #列名靠哪边显示,默认right
'''
display.column_space No description available.[default: 12] [currently: 12]
'''
'''
display.date_dayfirstboolean
    When True, prints and parses dates with the day first, eg 20/01/2005 [default: False] [currently: False]
'''
# pd.options.display.date_dayfirst = True          #
'''
display.date_yearfirstboolean
    When True, prints and parses dates with the year first, eg 2005/01/20 [default: False] [currently: False]
display.encodingstr/unicode
    Defaults to the detected encoding of the console. Specifies the encoding to be used for strings returned by to_string, these are generally strings meant to be displayed on the console. [default: utf-8] [currently: utf-8]
display.expand_frame_repr: boolean
    Whether to print out the full DataFrame repr for wide DataFrames across multiple lines, max_columns is still respected, but the output will wrap-around across multiple “pages” if its width exceeds display.width. [default: True] [currently: True]
    是否要自动换行,False不自动换行,横向也不会有滚动条,内容宽度在屏幕显示范围内可以False,超出屏幕范围最好设置成True(默认值)
'''
# pd.options.display.expand_frame_repr = False      #是否要自动换行
'''
display.float_formatcallable
    The callable should accept a floating point number and return a string with the desired format of the number. This is used in some places like SeriesFormatter. See formats.format.EngFormatter for an example. [default: None] [currently: None]
display.html.borderint
    A border=value attribute is inserted in the <table> tag for the DataFrame HTML repr. [default: 1] [currently: 1]
display.html.table_schemaboolean
    Whether to publish a Table Schema representation for frontends that support it. (default: False) [default: False] [currently: False]
display.html.use_mathjaxboolean
    When True, Jupyter notebook will process table contents using MathJax, rendering mathematical expressions enclosed by the dollar symbol. (default: True) [default: True] [currently: True]
'''
'''
display.large_repr: ‘truncate’/’info’
    For DataFrames exceeding max_rows/max_cols, the repr (and HTML repr) can show a truncated table (the default from 0.13), or switch to the view from df.info() (the behaviour in earlier versions of pandas). [default: truncate] [currently: truncate]
    打印的时候是截取表格部分数据(truncate)还是只显示表格的基本信息
'''
# pd.options.display.large_repr = 'info'          #打印时是显示信息还是,截取部分内容,默认truncate
'''
display.latex.escapebool
    This specifies if the to_latex method of a Dataframe uses escapes special characters. Valid values: False,True [default: True] [currently: True]
display.latex.longtable :bool
    This specifies if the to_latex method of a Dataframe uses the longtable format. Valid values: False,True [default: False] [currently: False]
display.latex.multicolumnbool
    This specifies if the to_latex method of a Dataframe uses multicolumns to pretty-print MultiIndex columns. Valid values: False,True [default: True] [currently: True]
display.latex.multicolumn_formatbool
    This specifies if the to_latex method of a Dataframe uses multicolumns to pretty-print MultiIndex columns. Valid values: False,True [default: l] [currently: l]
display.latex.multirowbool
    This specifies if the to_latex method of a Dataframe uses multirows to pretty-print MultiIndex rows. Valid values: False,True [default: False] [currently: False]
display.latex.reprboolean
    Whether to produce a latex DataFrame representation for jupyter environments that support it. (default: False) [default: False] [currently: False]
display.max_categoriesint
    This sets the maximum number of categories pandas should output when printing out a Categorical or a Series of dtype “category”. [default: 8] [currently: 8]
'''
'''
display.max_columns:int/None
    If max_cols is exceeded, switch to truncate view. Depending on large_repr, objects are either centrally truncated or printed as a summary view. ‘None’ value means unlimited.
    In case python/IPython is running in a terminal and large_repr equals ‘truncate’ this can be set to 0 and pandas will auto-detect the width of the terminal and print a truncated object which fits the screen width. The IPython notebook, IPython qtconsole, or IDLE do not run in a terminal and hence it is not possible to do correct auto-detection. [default: 0] [currently: 0]
    是否显示所有的列
'''
pd.options.display.max_columns = None           #设置显示的列数/所有列

'''
display.max_colwidth:int or None
    The maximum width in characters of a column in the repr of a pandas data structure. When the column overflows, a “…” placeholder is embedded in the output. A ‘None’ value means unlimited. [default: 50] [currently: 50]
display.max_info_columnsint
    max_info_columns is used in DataFrame.info method to decide if per column information will be printed. [default: 100] [currently: 100]
display.max_info_rowsint or None
    df.info() will usually show null-counts for each column. For large frames this can be quite slow. max_info_rows and max_info_cols limit this null check only to frames with smaller dimensions than specified. [default: 1690785] [currently: 1690785]
'''


'''
display.max_rows:int
    If max_rows is exceeded, switch to truncate view. Depending on large_repr, objects are either centrally truncated or printed as a summary view. ‘None’ value means unlimited.
    In case python/IPython is running in a terminal and large_repr equals ‘truncate’ this can be set to 0 and pandas will auto-detect the height of the terminal and print a truncated object which fits the screen height. The IPython notebook, IPython qtconsole, or IDLE do not run in a terminal and hence it is not possible to do correct auto-detection. [default: 60] [currently: 15]
    是否显示所有行,或指定最大可用显示的行数;
    1. None:无限制;
    2. 0: python自动根据屏幕高度显示行数
    3. 10以内的偶数,好像超过10,最大还是显示10行
'''
pd.options.display.max_rows = 8         #设置显示的行数: 0:自适应; 2~10的偶数; None:所有行
'''
display.max_seq_itemsint or None
    when pretty-printing a long sequence, no more then max_seq_items will be printed. If items are omitted, they will be denoted by the addition of “…” to the resulting string.
    If set to None, the number of items to be printed is unlimited. [default: 100] [currently: 100]
display.memory_usagebool, string or None
    This specifies if the memory usage of a DataFrame should be displayed when df.info() is called. Valid values True,False,’deep’ [default: True] [currently: True]
'''
'''
display.min_rows: int
    The numbers of rows to show in a truncated view (when max_rows is exceeded). Ignored when max_rows is set to None or 0. When set to None, follows the value of max_rows. [default: 10] [currently: 10]
'''
'''
display.multi_sparseboolean
    “sparsify” MultiIndex display (don’t display repeated elements in outer levels within groups) [default: True] [currently: True]
display.notebook_repr_htmlboolean
    When True, IPython notebook will use html representation for pandas objects (if it is available). [default: True] [currently: True]
display.pprint_nest_depthint
    Controls the number of nested levels to process when pretty-printing [default: 3] [currently: 3]
'''
'''
display.precision:int
    Floating point output precision (number of significant digits). This is only a suggestion [default: 6] [currently: 6]
'''
# pd.options.display.precision = 2        #小数点显示的位数
'''
display.show_dimensions:boolean or ‘truncate’
    Whether to print out dimensions at the end of DataFrame repr. If ‘truncate’ is specified, only print out the dimensions if the frame is truncated (e.g. not display all rows and/or columns) [default: truncate] [currently: truncate]
display.unicode.ambiguous_as_wide: boolean
    Whether to use the Unicode East Asian Width to calculate the display text width. Enabling this may affect to the performance (default: False) [default: False] [currently: False]
display.unicode.east_asian_width: boolean
    Whether to use the Unicode East Asian Width to calculate the display text width. Enabling this may affect to the performance (default: False) [default: False] [currently: False]
display.width:int
    Width of the display in characters. In case python/IPython is running in a terminal this can be set to None and pandas will correctly auto-detect the width. Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a terminal and hence it is not possible to correctly detect the width. [default: 80] [currently: 80]
io.excel.ods.reader: string
    The default Excel reader engine for ‘ods’ files. Available options: auto, odf. [default: auto] [currently: auto]
io.excel.ods.writer: string
    The default Excel writer engine for ‘ods’ files. Available options: auto, odf. [default: auto] [currently: auto]
io.excel.xls.reader: string
    The default Excel reader engine for ‘xls’ files. Available options: auto, xlrd. [default: auto] [currently: auto]
io.excel.xls.writer: string
    The default Excel writer engine for ‘xls’ files. Available options: auto, xlwt. [default: auto] [currently: auto]
io.excel.xlsb.reader: string
    The default Excel reader engine for ‘xlsb’ files. Available options: auto, pyxlsb. [default: auto] [currently: auto]
io.excel.xlsm.reader: string
    The default Excel reader engine for ‘xlsm’ files. Available options: auto, xlrd, openpyxl. [default: auto] [currently: auto]
io.excel.xlsm.writer: string
    The default Excel writer engine for ‘xlsm’ files. Available options: auto, openpyxl. [default: auto] [currently: auto]
io.excel.xlsx.reader: string
    The default Excel reader engine for ‘xlsx’ files. Available options: auto, xlrd, openpyxl. [default: auto] [currently: auto]
io.excel.xlsx.writer: string
    The default Excel writer engine for ‘xlsx’ files. Available options: auto, openpyxl, xlsxwriter. [default: auto] [currently: auto]
io.hdf.default_format:format
    default format writing format, if None, then put will default to ‘fixed’ and append will default to ‘table’ [default: None] [currently: None]
io.hdf.dropna_tableboolean
    drop ALL nan rows when appending to a table [default: False] [currently: False]
io.parquet.enginestring
    The default parquet reader/writer engine. Available options: ‘auto’, ‘pyarrow’, ‘fastparquet’, the default is ‘auto’ [default: auto] [currently: auto]
mode.chained_assignment: string
    Raise an exception, warn, or no action if trying to use chained assignment, The default is warn [default: warn] [currently: warn]
mode.sim_interactiveboolean
    Whether to simulate interactive mode for purposes of testing [default: False] [currently: False]
mode.use_inf_as_naboolean
    True means treat None, NaN, INF, -INF as NA (old way), False means None and NaN are null, but INF, -INF are not NA (new way). [default: False] [currently: False]
mode.use_inf_as_nullboolean
    use_inf_as_null had been deprecated and will be removed in a future version. Use use_inf_as_na instead. [default: False] [currently: False] (Deprecated, use mode.use_inf_as_na instead.)
plotting.backendstr
    The plotting backend to use. The default value is “matplotlib”, the backend provided with pandas. Other backends can be specified by providing the name of the module that implements the backend. [default: matplotlib] [currently: matplotlib]
plotting.matplotlib.register_converters: bool or ‘auto’.
    Whether to register converters with matplotlib’s units registry for dates, times, datetimes, and Periods. Toggling to False will remove the converters, restoring any converters that pandas overwrote. [default: auto] [currently: auto]
'''

# pd.options.display.max_rows = None

FilePath = r'.\testfile\testdata.csv'
data = pd.read_csv(FilePath,usecols=['Day',
                                     'Date',
                                     'T010001_Value',
                                     'T050003_Value',
                                     'T006009_1_Value',
                                     'T086002_1_Value',
                                     'T008033_Value'])
print(data)


exit()
'''get_option(param):需要一个参数(就是set_option()的参数)，并返回下面输出中给出的值'''
display_max_rows_initial = pd.get_option("display.max_rows")
print('Initial display_max_rows:',display_max_rows_initial)

'''set_option(param,value):需要两个参数，并将该值设置为指定的参数值'''
pd.set_option("display.max_rows",80)
display_max_rows_after = pd.get_option("display.max_rows")
print('After display_max_rows:',display_max_rows_after)


'''reset_option(param):接受一个参数，并将该值设置为默认值。'''
pd.reset_option("display.max_rows")
display_max_rows_reset = pd.get_option("display.max_rows")
print('Reset display_max_rows:',display_max_rows_reset)

'''describe_option(param):打印参数的描述。'''
pd.describe_option("display.max_rows")
























