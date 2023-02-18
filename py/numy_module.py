import numpy as np

'''创建数组'''
# a = np.array([[1,2,3],[4,5,6]])
# a = np.arange(1,7).reshape(2,3)
# print("arry a:",a,'*'*50,sep='\n')
'''查看数组的形状'''
# print("a shape:",a.shape)

'''resize():返回指定形状的新数组'''
# b = np.resize(a,(3,2))
# print("arry b:",b,'*'*50)
# print("b shape:",b.shape,'*'*50)


'''numpy.append(arr, values, axis=None):'''
'''
参数说明：
arr：输入数组
values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。
'''
# # axis无定义,返回一维数组
# c = np.append(a,[7,8,9])
# print("arry c(a append **,axis=None):",c,'*'*50,sep='\n')

# # 指定axis,0/1
# d = np.append(a,[[7,8,9]],axis=0)
# print("arry c(a append ** axis=0):",d,'*'*50,sep='\n')

# # 指定axis=1
# e = np.append(a,[[5,5,5],[7,8,9]],axis=1)
# print("arry c(a append **,axis=1):",e,'*'*50,sep='\n')

'''np.insert():函数在给定索引之前，沿给定轴在输入数组中插入值。'''
'''
arr：输入数组
obj：在其之前插入值的索引,要插入的位置
values：要插入的值,可以是列表,也可以是值
axis：沿着它插入的轴，如果未提供，则输入数组会被展开
'''
# aa = np.insert(a,3,[11,12,13]) #不指定axis,在插入之前输入数组会被展开
# print("insert [**] to a:",aa,'*'*50,sep='\n')

# bb = np.insert(a,1,[11],axis=0) #axis=0, 会广播值数组来配输入数组。沿轴 0 广播：
# print("沿0轴广播:",bb,'*'*50,sep='\n')

# cc = np.insert(a,1,11,axis=1)       #沿1轴广播
# print("沿1轴广播:",cc,'*'*50,sep='\n')

'''np.delete:函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。'''
'''
arr：输入数组
obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
'''
# aaa = np.delete(a,4)
# print("从a中删除位置为**的值:",aaa,'*'*50,sep='\n')

# bbb = np.delete(a,1,axis=1)
# print("从a删除第二列:",bbb,'*'*50,sep='\n')

# ff = np.array([1,2,3,4,5,6,7,8,9,10])
# print("ff arry:",ff,'*'*50,sep='\n')

# gg = np.delete(ff, np.s_[::2])  #进行切片删除,返回的是被删除的那部分
# print("对ff数组进行切片删除:",gg,'*'*50,sep='\n')

'''np.unique():去重'''
'''
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
'''
# mm = np.array([5,2,6,2,7,5,6,8,2,9])
# print("测试数组mm:",mm,'*'*50,sep='\n')

# nn = np.unique(mm)
# print("对数组mm去重:",nn,'*'*50,sep='\n')

# hh = np.unique(mm,return_index=True)
# print("对数组mm去重,return_index=True:新列表值在旧列表中的位置:",hh,'*'*50,sep='\n')

# ii = np.unique(mm,return_inverse=True)
# print("对数组mm去重,return_inverse=True:旧列表值在新列表中的位置:",ii,'*'*50,sep='\n')

# jj = np.unique(mm,return_counts=True)
# print("对数组mm去重,return_counts=True:元素在旧列表中出现的次数:",jj,'*'*50,sep='\n')

# oo,pp = jj = np.unique(mm,return_counts=True)   #当然也可以这么分开赋值
# print("分开赋值,去重数组:",oo,'*'*50,sep='\n')
# print("分开赋值,在旧列表里出现的次数:",pp,'*'*50,sep='\n')

'''np.sum()求和'''
# z = np.arange(1,9).reshape(2,4)
# print("示例源数组z:",z,'*'*50,sep='\n')

# zz = np.sum(z)
# print("sum不指定axis:",zz,'*'*50,sep='\n')

# zz = np.sum(z,axis=0)
# print("sum聚合axis=0:",zz,'*'*50,sep='\n')

# xx = np.sum(z,axis=1)
# print("sum聚合axis=1:",xx,'*'*50,sep='\n')

'''np.concatenate():链接,横着连/竖着连'''
# k1 = np.arange(1,7).reshape(2,3)
# k2 = np.arange(5,11).reshape(2,3)
# print("示例源数组k1:",k1,'*'*50,sep='\n')
# print("示例源数组k2:",k2,'*'*50,sep='\n')

# kk = np.concatenate([k1,k2])
# print("K1K2,axis不指定:",kk,'*'*50,sep='\n')

# kk = np.concatenate([k1,k2],axis=0)
# print("K1K2,axis=0:",kk,'*'*50,sep='\n')

# kk = np.concatenate([k1,k2],axis=1)
# print("K1K2,axis=1:",kk,'*'*50,sep='\n')

'''np.ndarray.flatten():展平,返回一份数组拷贝，对拷贝所做的修改不会影响原始数组'''
'''
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
'''
# org = np.arange(15).reshape(3,5)
# print("示例数组org:",org,'*'*50,sep='\n')

# flatten = org.flatten()
# print("org.flatten,order默认:",flatten,'*'*50,sep='\n')

# flattenf = org.flatten(order='F')
# print("示例数组org:",flattenf,'*'*50,sep='\n')

'''np.ravel(a,order=c):展平(方法同flatten),返回源数组视图,修改会影响原始数组'''
'''
a: 需要展平的数组
order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
'''

'''np.transpose():同np.ndarry.T, 数组翻转'''
# org = np.arange(15).reshape(3,5)
# print("示例数组org:",org,'*'*50,sep='\n')

# # # trans = np.transpose(org)
# # # trans = org.transpose()
# trans = org.T
# print("transpose:",trans,'*'*50,sep='\n')

'''numpy.rollaxis 函数向后滚动特定的轴到一个特定位置，格式如下：'''
'''
参数说明：
    arr：数组
    axis：要向后滚动的轴，其它轴的相对位置不会改变
    start：默认为零，表示完整的滚动。会滚动到特定位置。
'''
# org = np.arange(24).reshape(3,2,4)
# print("示例数组org:",org,'*'*50,sep='\n')

# roll20 = np.rollaxis(org,2,start=0)
# print("轴2滚动到轴0:",roll20,'*'*50,sep='\n')

# roll21 = np.rollaxis(org,1,start=0)
# print("轴1滚动到轴0:",roll21,'*'*50,sep='\n')

'''np.reshape():重新整型'''
'''
1、a : 数组——需要处理的数据。

2、newshape : 新的格式——整数或整数数组，如(2,3)表示2行3列。新的形状应该与原来的形状兼容，即行数和列数相乘后等于a中元素的数量。如果是整数，则结果将是长度的一维数组，所以这个整数必须等于a中元素数量。若这里是一个整数数组，那么其中一个数据可以为-1。在这种情况下，这个个值python会自动从根据第二个数值和剩余维度推断出来。

3、order的情况相比于前面两个参数有些复杂，这里会用比较大的篇幅来解释，并在后面给出一个比较易懂的示例

    首先做出翻译：order : 可选范围为{‘C’, ‘F’, ‘A’}。使用索引顺序读取a的元素，并按照索引顺序将元素放到变换后的的数组中。如果不进行order参数的设置，默认参数为C。

（1）“C”指的是用类C写的读/索引顺序的元素，最后一个维度变化最快，第一个维度变化最慢。以二维数组为例，简单来讲就是横着读，横着写，优先读/写一行。

（2）“F”是指用FORTRAN类索引顺序读/写元素，最后一个维度变化最慢，第一个维度变化最快。竖着读，竖着写，优先读/写一列。注意，“C”和“F”选项不考虑底层数组的内存布局，只引用索引的顺序。

（3）“A”选项所生成的数组的效果与原数组a的数据存储方式有关，如果数据是按照FORTRAN存储的话，它的生成效果与”F“相同，否则与“C”相同。这里可能听起来有点模糊，下面会给出示例。
'''
# org = np.arange(24).reshape(3,8)      #reshape给两个参数,代表创建的是二维数组
# org = np.arange(24).reshape(2,3,4)    #reshape给三个参数,此处意思是创建2个3x4的二维数组,就是三维数组了
# print("示例数组:",org,'*'*50,sep='\n')

'''np.swapaxes():交换数组的两个轴'''
'''
arr：输入的数组
axis1：对应第一个轴的整数
axis2：对应第二个轴的整数
'''
# org = np.arange(24).reshape(3,2,4)
# print("示例数组org:",org,'*'*50,sep='\n')

# swp = np.swapaxes(org,2,0)
# print("0,2轴交换后:",swp,'*'*50,sep='\n')

'''np.broadcast:产生模仿广播的对象'''


