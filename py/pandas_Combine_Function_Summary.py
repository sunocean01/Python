'''此脚本用来介绍pandas对DataFrame合并的相关函数: append,concat,merge,combine,join'''


import pandas as pd

pd.options.display.max_columns = None       #None:显示的列没有限制;也可以给具体的数字,指定具体显示的列数;
pd.options.display.max_rows = None          #同上
# pd.options.display.max_colwidth = 1
pd.options.display.expand_frame_repr = False    #Bool,是否要自动换行


df1_file = r'.\testfile\Pandas_Combine_Function_Summary\df1.txt'
df2_file = r'.\testfile\Pandas_Combine_Function_Summary\df2.txt'
df3_file = r'.\testfile\Pandas_Combine_Function_Summary\df3.txt'
df4_file = r'.\testfile\Pandas_Combine_Function_Summary\df4.txt'

df1 = pd.read_csv(df1_file,sep='\t',index_col=0)
print('df1:',df1,'-'*80,sep='\n')
'''df1 VS df2:列名完全相同,行标有重复;不同的行标整行值有重复'''
df2 = pd.read_csv(df2_file,sep='\t',index_col=0)
print('df2:',df2,'-'*80,sep='\n')
'''df1 VS df3:部分列名不一样,行标有重复,有一行是完全一样的,有一行索引是一样的,行里的值不完全一样'''
df3 = pd.read_csv(df3_file,sep='\t',index_col=0)
print('df3:',df3,'-'*80,sep='\n')

'''df4 VS df1: 所有内容都不同'''
df4 = pd.read_csv(df4_file,sep='\t',index_col=0)
print('df4:',df4,'-'*80,sep='\n')


'''DataFrame.append():1. 列对齐,列名相同的放在同一列,2. 只能往0轴方向合并; 3. 可以同时合并单个或多个DataFrame'''
'''
other: 是要添加的数据，append很不挑食，这个other可以是dataframe，dict，Seris，list等等;可以是列表,同时合并多个。
ignore_index: 默认False,参数为True时将在数据合并后，按照0，1，2，3....的顺序重新设置索引，忽略了旧索引。
verify_integrity：参数为True时，如果合并的数据与原数据包含索引相同的行，将报错。
    　　如果是True，不能容忍合并的DataFrame的index 有重复; 如果ignore_index=True，索引也不存在重复的情况；
    　　如果是False，是允许合并的DataFrame的index重复，这是默认值
sort: 如果是True：将会对columns排序， 默认是False;最新版提示没有默认值
'''

# df1Adf2 = df1.append(df2,
                     # ignore_index=False,        #bool,False(默认)时,保持各自的行索引;True时,忽略原行索引,重新附给0,1,2,3...的行索引
                     # verify_integrity=True,    #bool,合并后允(即ignore_index执行后)不允许有重复的行索引,False:允许;True:不允许
                     # sort=False)
# print("df1Adf2_append:",df1Adf2,sep='\n')
# --------------------------
'''df1+df3:append会对列标进行对齐,df1,df3都有的列,会将df3的值添加到df1的下面,df3有,df1没有的,会将df3的列作为新列添加'''
# df1Adf3 = df1.append(df3,sort=False)
# print("df1Adf3_append",df1Adf3,sep='\n')

'''同时合并多个表'''
# df1Adf2Adf3 = df1.append([df2,df3],sort=False)
# print('df1Adf2Adf3:',df1Adf2Adf3,sep='\n')

'''pd.concat():拼接,横向或纵向拼接,可以同时对多个表进行合并, 不管往哪个方向拼,都是以索引对齐,即相同索引名的放在一列/行'''
'''
obj：要合并的series，dataframe或者是panel构成的序列，常将这些数据排成一个列表[data1,data2....]。
axis：按照哪个方向拼接，0是纵向拼接（默认），1是横向拼接。
join：设置合并取交集（inner）还是并集（outer）。纵向拼接时取column的交并集，横向拼接时取index的交并集。
join_axes：[df1.index]index的列表，仅在横向合并时使用，指明要将数据合并入哪个原表的index。
ignore_index：如果设置为true，则无视表的index，直接合并，合并后生成新的index。
keys：表标识的列表，用来区分合并的表来自哪里。
sort: 要不要排序,有时候必须指定
'''

df1Adf2 = pd.concat([df1,df2],
                            axis=1,                 #往哪个方向拼, 不管哪个方向拼,都是以索引对齐,它允许列名重复
                            # sort=True,              #是否排序
                            # join='outer',           #取交还是取并
                            # ignore_index=False,     #是否忽视原索引
                            # # keys=['df1','df3'],     #注明数据来源
                            # # # join_axes=[df1.index]   #指定根据那个表的轴拼接,貌似已经取消
                            )
print('df1Adf3_concat:',df1Adf2,sep='\n')



'''pd.merge():合并两个表格,'''
'''
left: 第一个DataFrame
right:第二个DataFrame
on：列名，join用来对齐的那一列的名字，用到这个参数的时候一定要保证左表和右表用来对齐的那一列都有相同的列名。
    如果两组数据需要对齐的列名不相同，则使用：
    left_on：左表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
    right_on：右表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
left_index/ right_index: 如果是True的haunted以index作为对齐的key
how：数据融合的方法。
    left:只取左侧key的值
    right:只取右侧key的值
    outer:取并集
    inner: 默认取交集
sort：根据dataframe合并的keys按字典顺序排序，默认是False，如果置false可以提高表现。
suffixes: 字符串元组，用于追加到重叠列的末尾，默认为('_x','_y').
copy: 设置为False，可以在某些特殊情况下避免将数据复制到结果数据结构中。默认总是复制。
'''

'''基本的合并逻辑理解:
可以实现的合并方式:
优点:
1. 在选择对齐的列时更灵活;
2. 
缺点:
1. 只能横着拼;
'''
# df1Adf2 = pd.merge(df1,df2,
                    
                    # on = 'T004001_Value',   #共有列,以该列对齐,然后进行横向拼接,自动给重复的列名加后缀_x,_y
                    
                    # # left_on = 'T008017_Value',             #df1需要用来对齐的列, 要对齐的列名在两个DataFrame中不相同时使用,代替on参数
                    # # right_on = 'T008018_Value',            #df2需要用来对齐的列, 要对齐的列名在两个DataFrame中不相同时使用,代替on参数
                    
                    # # left_index = True,          #是否用行索引来对齐
                    # # right_index = True,         #是否用行索引来对齐
                                        
                    # how = 'inner',          #left,right,outer,inner,
                    
                    # sort = False,
                    
                    # suffixes = ('_mg1','_mg2'),     #给重名的列名加的后缀
                    # )

# print('df1Adf2_merge:',df1Adf2,sep='\n')

'''df1和df4:完全不同'''
# df1Adf4 = pd.merge(df1,df4,
                    # left_index = True,
                    # right_index = True,
                    
                    # how = 'outer',
                        # )
# print('df1Adf4_merge:',df1Adf4,sep='\n')


'''combine(): 列名对齐,逐列按条件取舍'''
'''
other ： DataFrame
        要按列合并的DataFrame。
func ： 功能:将两个系列作为输入并返回一个Series或一个标量的函数。用于逐列合并两个数据帧。
fill_value ： 标量值，默认None,在将任何列传递给合并函数之前填充NaN的值。
overwrite ： boolean，默认为True,如果为true，列自我不存在在其他将与NaN的覆盖
'''
# df1_combine = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
# df2_combine = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
# print('df1_combine:',df1_combine,sep='\n')
# print('df2_combine:',df2_combine,sep='\n')

# take_smaller = lambda s1, s2: s1 if s1.sum() < s2.sum() else s2           #s1,s2是逐列转递
# df_combine = df1_combine.combine(df2_combine, take_smaller)
# print('df_combine:',df_combine,sep='\n')

'''join():横着拼且不允许列名重复,通过对齐行索引或者指定的对齐的列连接两个DataFrame。通过一个list可以一次高效的连接多个'''
'''
other:【DataFrame，或者带有名字的Series，或者DataFrame的list】如果传递的是Series，那么其name属性应当是一个集合，并且该集合将会作为结果DataFrame的列名
on:【列名称，或者列名称的list/tuple，或者类似形状的数组】连接的列，默认使用索引连接, 已经提示只能用索引对齐
how:【{‘left’, ‘right’, ‘outer’, ‘inner’}, default: ‘left’】连接的方式，默认为左连接
lsuffix:【string】左DataFrame中重复列的后缀,没有默认值,必须赋值
rsuffix:【string】右DataFrame中重复列的后缀,没有默认值,必须赋值
sort:【boolean, default False】按照字典顺序对结果在连接键上排序。如果为False，连接键的顺序取决于连接类型（关键字）。
注:
1. 当需要join的数据是DataFrame的list时，不支持传递参数on，lsuffix，sort
2. 通过on参数指定连接的列，DataFrame.join总是使用other的索引去连接caller，因此我们可以把指定的列设置为other的索引，然后用on去指定caller的连接列，这样可以让连接结果的索引和caller一致

链接：https://www.jianshu.com/p/2358d4013067
'''

'''默认使用index索引连接且是左连接,有重复列名,lsuffix和rsuffix没有默认值'''
# df1Adf2_join = df1.join(
                        # df2,
                        # how = 'outer',
                        # lsuffix='_df1',
                        # rsuffix='_df2'
                            # )

# print("df1Adf2_join:",df1Adf2_join,sep='\n')

# df1Adf3 = df1.join(df3,lsuffix='_a',rsuffix='_b',how='outer')
# print('df1Adf3:',df1Adf3,sep='\n')


