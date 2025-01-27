#!/usr/bin/env python3
import sys
import xlrd
import xlwt
import xlutils
import xlwings as xw

app = xw.App(visible=True,add_book=False)
"""
打开excel程序，默认设置：程序可见，打开并新建一个工作簿，一个工作表；即：xw.App()=xw.App(visible=True,add_sheet=True)
visible
Ture：可见excel
False：不可见excel
也就是处理Excel的过程会不会显示出来

add_book
True:打开excel并且新建工作簿
False：不新建工作簿
也就是是不是打新建一个新的工作簿
"""

app.display_alerts = False
#是否提示警告信息，True or False

app.screen_updating = False
# 选项，是配置是否实时刷新excel程序的显示内容，如果配是True，我实测会导致速度慢三倍左右。

format = sys.argv[1]
#将外部输入的文件地址附给变量format;

wb = xw.Book()

# wb = xw.Book()  # this will create a new workbook，如果App()中add_book=True,此步是否可以省略？
# wb = xw.Book('FileName.xlsx')  # connect to an existing file in the current working directory
# wb = xw.Book(r'C:\path\to\file.xlsx')  # on Windows: use raw strings to escape backslashes
# wb = app.books.open('file.xlsx')  #直接打开文件后，不可见；
'''
以上是创建或打开excel工作簿的方法，实测可以直接用以上方式创建和打开excel文件，
可以不需要用xw.App()先打开excel程序；
'''

# xw.apps[10559].books['FileName.xlsx']
'''
If you have the same file open in two instances of Excel, 
you need to fully qualify it and include the app instance. 
You will find your app instance key (the PID) via xw.apps.keys():
xw.apps[10559].books['FileName.xlsx']
如果你要在两个App中打开同一个文件，你需要完全限定该文件且包括程序实例，
-->见xlwings中设计的模型概念层级；xlwings >> App >> Book >> Sheet >> Range
'''

new_sht = wb.sheets.add('format')
# 向工作簿中添加新的工作表'format';

shts = wb.sheets
#wb.sheets 实际上返回的是工作簿中所有工作表名称的列表；

sht = wb.sheets[0]
#按位置好索引工作表；

format_sht = wb.sheets['format']
# 按照工作表名称索引工作表；

format_sht.range('A1').value = 'Hello word!'
# 向工作表的A1单元格中写入内容；注：'A1'或'a1'都可以，不区分大小写；

format_sht.range('b1').value = [['foo1','foo2','foo3'],[10,20.0,30.00]]
# range()代表矩阵的意思，如果只输入一个参数那就是矩阵的左上角单元格位置，也可以指定两个参数即矩阵的左上角和右下角单元格位置；

format_sht['a1:a5'].value = [1,2,35,6,9]
#

#引用活动工作表单元格或区域方式如下：
'''
xw.Range('A1')
xw.Range('A1:C3')
xw.Range((1,1))
xw.Range((1,1), (3,3))
xw.Range('NamedRange')
xw.Range(xw.Range('A1'), xw.Range('B2'))
'''

format_sht.api.Copy(Before=wb.sheets[0].api) #将复制的工作表放到指定工作表之前；此例是放置最开始
# format_sht.api.Copy(None,After = wb.sheets[-1].api) #将复制的工作表放到指定工作表之后；

new_sht = wb.sheets[-1] #将工作簿中最后一个工作表附给变量

new_sht_name = 'CP_CN_202002-02'    #起一个名字

new_sht.api.name = new_sht_name     #工作表改名为这个新名字



wb.save(r'C:\Users\osun\Desktop\Python\test\test.xlsx')
# 将新建的工作表命名为test并保存在该地址


wb.close()

wb.quit()








