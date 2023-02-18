"""本实例介绍tkinter模,就像画画一样"""



import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


window = tk.Tk()    #先铺一张画布

window.title("My First 'tk'")   #给画布起个名字

window.geometry("1000x2000")      #画布尺寸


'''Label:标签部件'''
L = tk.Label(master=window,
            anchor='center',         #文本在标签中的位置:n,s,w,e,ne,nw,sw,se,center
            justify = 'left',   #有多行文本时的对齐方式: left,right,center, 默认center
            text="Hello tk \n hello python",
            # textvariable = StringVar  #?
            bg="yellow",
            # bd=10,             #像素大小
            font=('Arial',14,'bold italic underline'),  #字体型号,大小,形状
            width=20,       #标签的宽
            heigh=2,        #标签的高
            cursor = 'cross',       #鼠标到这个位置的形状 arrow, circle, cross, plus
            fg = 'red',     #字体颜色
            # image = r'.\testfile\pic.gif',      #怎么用?
            padx = 100,         #x 轴间距，以像素计，默认 1。
            pady = 10,          #影响标签的高度;
            relief = 'sunken',      #标签边框样式:FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
            borderwidth = 2,    #边框宽度,通常1或2
            underline = 1,      #int,数字,即第几个字母下面有下划线
            wraplength = 0      #设置标签文本为多少行显示，默认为 0。
            # activebackground = ,
            # activeforeground = ,
                        
            )


L.pack(
    # anchor='n',     #"n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 默认"center" 
    # expand=True,    #Bool, 指定是否填充父组件的额外空间,默认False
    fill = 'x',     #指定是否填充父组件的额外空间,默认False,还可以是 x,y和both
    # in_ = '',       #将该组件放到该选项指定的组件中,指定的组件必须是该组件的父组件
    # ipadx = 10,      #指定水平方向上的内边距
    # ipady = 10,     #指定垂直方向上的内边距
    padx = 10,      #指定水平方向上的外边距
    pady = 200,      #指定垂直方向上的外边距
    side = 'right',  # 指定组件的放置位置,默认值是 "top";还可以设置的值有："left"，"bottom"，"right"
    
    )    #放置标签


'''Button窗口部件'''
# 定义一个函数功能,供点击Button按键时调用,调用参数: commond="函数名"
def press_me():
    # print("I am pressed!")
    # tk.messagebox.showinfo(title='Hi',message='你好')
    # tk.messagebox.showwarning(title='Hi',message='警告')
    # tk.messagebox.showerror(title='Hi',message='警告')
    # tk.messagebox.askquestion(title='Hi',message='是否继续?')
    tk.messagebox.askyesno(title='Hi',message='是/否?')

b = tk.Button(window,
    activebackground='orange',  #鼠标点击该按钮的时候会显示的颜色
    # avtiveforeground='green',   #报错?? 当鼠标放上去时，按钮的前景色
    bd = 10,            #按钮边框的大小，默认为 2 个像素
    bg = 'orange',      #按钮的背景颜色
    text='hit me',
    fg = 'blue',        #按钮文本的颜色
    # highlightcolor='purple',    #高亮颜色
    # image=r'C:\Users\osun\Desktop\Python\Function\testfile\pic.gif',    #??? 按钮上要显示的图片
    # justify = 'left',   #显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
    # padx = 40,   #按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离
    # pady = 10,   #按钮在y轴方向上的内边距(padding)
    font=('Arial',12),
    width=10,           #按钮的宽度，如未设置此项，其大小以适应按钮的内容（文本或图片的大小）
    height=1,           #按钮的高度
    relief = 'raised',  #边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
    state = 'disabled',   #设置按钮组件状态,可选的有NORMAL(可以点)、ACTIVE、 DISABLED(按钮被锁住,点不了)。默认 NORMAL。
    underline = 3,      #下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推
    wraplength=50,       #限制按钮每行显示的字符的数量,应该按钮每行总的可显示的字符数量;
    anchor='center',         #锚选项，控制文本的位置，默认为中心,可选值:"n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center"
    command=press_me        #当按钮被点击时，执行该函数
    )    #在窗口界面设置放置Button按键
b.pack(
    anchor='w',
    side='left',
    padx = 50,
    )

'''Entry窗口部件: 一个单行文本输入域'''
e1 = tk.Entry(window,
    bg = 'white',   #输入框背景颜色
    bd = 4,         #边框的大小,默认2个像素;
    cursor = 'plus',   #光标的形状设定，如arrow, circle, cross, plus 等
    font=('Arial',14),  #文本字体;
    exportselection=0,  #???默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
    fg='red',           #文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
    # highlightcolor='',  #文本框高亮边框颜色，当文本框获取焦点时显示
    justify='left',     #显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
    relief='sunken',    #边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
    selectbackground='blue', #选中文字的背景颜色
    selectborderwidth=5,    #选中文字的背景边框宽度
    selectforeground='black', #选中文字的颜色
    show='-',        #指定文本框内容显示为字符，值随意，满足字符即可。如密码可以将值设为 show="*"
    state='normal',#默认为 state=NORMAL, 文框状态，分为只读和可写，值为：normal/disabled
    # textvariable='',    #文本框的值，是一个StringVar()对象
    width=5,       #文本框宽度
    )    #显示成密文形式
    
e2 = tk.Entry(window,font=('Arial',14),show='*')   #显示成明文形式

e1.pack()
e2.pack()

e2.insert("insert","python test, ")   #向文本框中插入内容
e2.icursor(2)                       #将指针移动到第二个字符后面,就是y的后面
e2.insert("insert","again")         #再次插入内容
# ----------------------------
# e2.selection_from(2)                #选中文本的开始点
# e2.selection_to(6)                  #选中文本的结束点
# ---------------------------
# e2.selection_range(1,5)             #选中输入框的内容
print(e2.selection_present())       #bool,文本框的内容是否有被选中的

def gt():
    txt = e2.get()                  #获取文本框中的内容
    print(txt)

but = tk.Button(window,
        text='确认',
        width=30,
        height=2,
        command=gt,
            )
but.pack()


'''Text窗口部件:一个多行文本区域'''
t = tk.Text(            #大部分参数同Entry, 没有justify,show
    window,
    bg='white',
    bd = 5,
    cursor='circle',
    font=('Arial',16),
    # exportselection=1,
    fg = 'orange',
    relief='raised',
    selectbackground='red',
    selectborderwidth=30,
    selectforeground='green',
    state='normal',
    width=600,    
    height=4)
t.pack(
    anchor='e',
    padx=50,
    # side='left'
    )
t.insert("insert","this is text txt,\n,again")       #向文本框中插入内容;
t.insert(2.3,"second insert")
t.insert(tk.END,"\n tk.END")

print("bbox:",t.bbox(1.2))      #? 为什么返回None
print("compare:",t.compare(1.2,"<",1.5))    #指定文本框里两个字符比较
print("Debug:",t.debug(boolean=True))
# t.delete(1.2,1.6)           #删除第一行第二个到第六个字符
print(t.dump(1.2,1.6))
t.mark_set("here",1.5)
print("mark_previous:",t.mark_previous(2.1))


def fetchText():
    content = t.get('1.0','1.end')        #获取文本框中的内容
    print(content)


bt = tk.Button(window,
        text='Confirm',
        width=30,
        height=2,
        command=fetchText,
            )
bt.pack(

    # anchor='e',
    # padx=50,
    # side='left'
    )

# 创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(window, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)     # 设置下拉列表的值
numberChosen.pack()      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

'''Listbox窗口部件'''
var1 = tk.StringVar()   #创建变量,用var1用来接收鼠标点击具体选项的内容
L2 = tk.Label(window,bg="yellow",fg="Red",font=('Arial',12),width=10,textvariable=var1)
L2.pack()

# 创建一个方法用于按钮的点击事件
def print_selection():
    value = lb.get(lb.curselection())    #获取当前选中的文本
    var1.set(value)
    print("value:",value)
    print("curselection:",lb.curselection())
b2 = tk.Button(window,text="print selection",width=15,height=2,command=print_selection)
b2.pack()

#添加一个滚动条
sb = tk.Scrollbar(window)
sb.pack(side="right",fill="y")


# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set((1,2,'egg'))
lb = tk.Listbox(window,
    background="green", #或者bg,背景颜色
    cursor="cross",          #指定当鼠标在 Listbox 上飘过的时候的鼠标样式
    exportselection=False,  #默认True, 允不允许选中的文本被复制到剪贴板
    font=("Arial",14),      #字体设定
    foreground="red",       #或fg,字体颜色
    height=1,               #Listbox显示的行数,不是像素
    width=30,               #设置Listbox的宽度
    listvariable=var2,      #为Listbox添加内容
    relief="flat",
    selectbackground="black",   #被选中时的背景颜色
    selectborderwidth=10,       #指定当某个项目被选中的时候边框的宽度
    selectforeground="yellow",  #指定当某个项目被选中的时候文本颜色
    selectmode="extended",      #选择模式:"single"（单选）、"browse"（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现）
    setgrid=False,               #指定一个布尔类型的值，决定是否启用网格控制
    # takefocus=True,             #bool,指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来）
    # xscrollcommand=,
    # yscrollcommand=,
    )   #指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目,2. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("鸡蛋 鸭蛋 鹅蛋 李狗蛋")

# 创建一个list并将值循环添加到Listbox控件中
list_items = [11,22]
for item in list_items:
    lb.insert('end',item)
lb.insert(0,'first')            #insert(index, *elements)
lb.insert(2,'second')
lb.insert(tk.END,'end')
# lb.delete(0,3)        # delete(first, last=None)

print("bbox:",lb.bbox(2))   # 返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)
print("curselection:",lb.curselection())    #返回一个元组，包含被选中的选项的序号（从 0 开始）,需要和Button结合使用,和get(lb.curselection())获取值;
print("get:",lb.get(3,5))
print("index:",lb.index(5))         #不知道有啥用
lb.itemconfig(4, fg='gray', selectforeground="gray")    #对指定字符属性设置
print("itemcget:",lb.itemcget(4,'background'))  #? itemcget(index, option),-- 获得 index 参数指定的项目对应的选项（由 option 参数指定）
lb.scan_mark(2,5)
sb.config(command=lb.yview)     #配置滚动条

lb.pack()

'''Radiobutton窗口部件:单选项按钮'''
var3 = tk.StringVar()
L3 = tk.Label(window,bg="yellow",width=20,text="empty")
L3.pack()

def print_selection2():
    L3.config(text=str(var3.get())+" is selected ")

r1 = tk.Radiobutton(window,
        activebackground="blue",    #设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的背景色, 就是选中的一瞬间
        activeforeground="red",
        anchor="nw",                  #"n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位
        background="orange",            #或bg,背景颜色
        borderwidth=10,                 #或bd
        cursor="cross",                 #鼠标形状
        disabledforeground="black",     #指定当 Radiobutton 不可用的时候前景色的颜色
        font=("bolder",16),             #字体和大小
        height=3,                       #设置 Radiobutton 的高度
        width=10,
        indicatoron=False,              #默认True,是圆点,False: 凸凹按钮
        justify="right",                #如何对齐多行文本, "left"，"right" 或 "center",文本位置取决于anchor选项;
        padx = 2,                       #指定 Radiobutton 水平方向上的额外间距（内容和边框间）
        pady = 3,
        relief="sunken",                #指定边框样式, "sunken"，"raised"，"groove"，"ridge" 或 "flat"
        selectcolor="red",              #选择后的底色
        # state="disabled",               #指定 Radiobutton 的状态,2. 默认值是 "normal",3. 另外你还可以设置 "active" 或 "disabled"
        takefocus=True,                 #如果是 True，该组件接受输入焦点（用户可以通过 tab 键将焦点转移上来）. 默认值是 False
        text="Option A",
        # textvariable=StringVar,       #Radiobutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容
        variable=var3,
        value="A",
        command=print_selection2,       #指定于该按钮相关联的函数或方法
        )
r1.select()     #为什么必须有一个设定为选中状态,其他的才可以设置成不被选中状态
r1.pack()
r2 = tk.Radiobutton(window,text="Option B", variable=var3,value="B",command=print_selection2)
r2.deselect()
# r2.flash()
r2.pack()

r3 = tk.Radiobutton(window,text="Option C", variable=var3,value="C",command=print_selection2)
r3.deselect()
r3.pack()

'''Checkbutton窗口部件:多选按钮'''
# 在画布上创建一个标签
L4 = tk.Label(window,
            bg="white",
            width=20,
            text="empty",
            )
L4.pack()

# 定义触发函数功能
def print_selection3():
    if(var5.get() == 1) & (var4.get() == 0):
        L4.config(text="I love only Python")
    elif(var5.get() == 0) & (var4.get() == 1):
        L4.config(text="I love C")
    elif(var5.get() == 0) & (var4.get() == 0):
        L4.config(text="Don't love both")
    else:
        L4.config(text="Both")

# 定义两个Checkbutton并放置
var5 = tk.IntVar()
var4 = tk.IntVar()
c3 = tk.Checkbutton(window,text="Python",variable=var5,onvalue=1,offvalue=0,command=print_selection3)
c3.pack()
c4 = tk.Checkbutton(window,
                    activebackground="blue",
                    activeforeground="red",
                    font=("Arial",14),
                    fg="black",
                    bg="grey",
                    cursor="cross",
                    height=3,
                    width=10,
                    justify="left",
                    text="c",
                    variable=var4,
                    onvalue=1,
                    offvalue=0,
                    # state="disabled",
                    padx=2,
                    pady=3,
                    selectcolor="black",
                    # variable= ,
                    command=print_selection3,
                    )
c4.select()
c4.pack()




'''Scale窗口部件:滑动条'''
# 创建标签用以显示并放置
L5 = tk.Label(window,bg="orange",fg="white",width=20,text='')
L5.pack(side="left")

# 定义一个触发函数功能
def print_selection4(v):
    L5.config(text=v + " is selected")

# 创建一个尺度滑条,长度200字符,0~10,以2为刻度,精度0.01,触发调用print_selection4函数
s = tk.Scale(window,
                label="try me",
                from_=0,
                to=10,
                resolution=2,       #滑动条步长
                showvalue=1,    #是否显示当前值,
                # label=            #?
                
                orient=tk.HORIZONTAL,   #VERTICAL 和 HORIZONTAL 两个值
                length=200,     #轨道长度
                width=20,        #轨道宽度
                # sliderrelief=,  #设置滑块立体样式
                troughcolor="red",  #轨道颜色
                tickinterval=2,
                digits=2,
                command=print_selection4)
s.pack(side="right")


'''Canvas窗口部件'''
# 创建一个画布并放置各种元素
canvas = tk.Canvas(window,bg="green",height=50,width=500)

# 说明图片位置,并导入图片到画布上
image_file = tk.PhotoImage(file=r".\testfile\pic.gif",)
image = canvas.create_image(25,0,anchor='nw',image=image_file)

# 定义多边形参数,然后在画布上画出指定图形
x0,y0,x1,y1 = 100,100,150,150
line = canvas.create_line(x0-50,y0-50,x1-50,y1-50)
oval = canvas.create_oval(x0+120,y0+120,x1+120,y1+50,fill='yellow')
arc = canvas.create_arc(x0,y0+50,x1,y1+50,start=0,extent=180)
rect = canvas.create_rectangle(330,30,330+20,30+20)
canvas.pack()

# 触发函数,用来一定指定图形
def moveit():
    canvas.move(arc,2,2)    #移动弧形,每次按(x=2,y=2)的步长移动

b3 = tk.Button(window,text="move",command=moveit).pack()

'''Menu窗口部件:头部菜单选项'''
# 创建一个标签并放置
L6 = tk.Label(window,text='None',bg='green')
L6.pack()

# 定义一个函数功能,用来代表菜单选项功能,这里为了操作简单,定义的功能比较简单
counter = 0
def do_job():
    global counter
    L6.config(text='do '+str(counter))
    counter += 1

# 创建一个菜单栏,这里我们可以理解成一个容器,在窗口上方
menubar = tk.Menu(window)
# 创建一个file菜单项(默认步下拉,下拉内容包括New,open,Save,Exit功能项)
filemenu = tk.Menu(menubar,tearoff=0)
# 将上面定义的空菜单命名为File,放置菜单中,就是装入哪个容器
menubar.add_cascade(label='File',menu=filemenu)
# 在File中加入New,Open,Save等小菜单,
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()    #添加一条分割线
filemenu.add_command(label='Exit',command=window.quit)  #tkinter里面自带的函数

# 创建一个Edit菜单(默认不下拉,下拉内容包括Cut,Copy,Paste等)
editmenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)

# 在Edit中加入小菜单
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

# 创建第二级菜单,即菜单里面的菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
# 创建第三级菜单命令,即菜单里面的菜单命令
submenu.add_command(label='Submenu_1',command=do_job)

# 菜单创建完成后,配置让菜单栏menubar显示出来
window.config(menu=menubar)


'''Frame窗口部件'''
# 创建一个标签并放置
# tk.Label 

# 创建第二层框架frame,长在主框架Frame上面
# frame_l = tk.Frame(frame)   #第二层frame,左frame,长在主Frame上面
# frame_r = tk.Frame(frame)
# frame_l.pack(side='left')
# frame_r.pack(side='right')

# 创建三组标签,为第二层frame上的内容,分为左区域和右区域
# tk.Label(frame_l,text='on the frame_l1',bg='green').pack()
# tk.Label(frame_l,text='on the frame_l2',bg='green').pack()
# tk.Label(frame_l,text='on the frame_l3',bg='green').pack()
# tk.Label(frame_r,text='on the frame_r1',bg='yellow').pack()
# tk.Label(frame_r,text='on the frame_r2',bg='yellow').pack()
# tk.Label(frame_r,text='on the frame_r3',bg='yellow').pack()

# form = tk.Frame(window)
# form.pack(side="right")

'''messageBox窗口部件:点击按钮后会弹出对话框'''
# 见22行,Button窗口部件

'''窗口部件三种放置方式pack/grid/place'''
# 1. Grid(已经被pack取代): grid是方格,所以所有的内容会被放在这些规律的方格中,如:

# 2. Pack: 按照上下左右的方式排列
tk.Label(window,text='p',fg='red').pack(side='top')
tk.Label(window,text='p',fg='red').pack(side='bottom')
tk.Label(window,text='p',fg='red').pack(side='left')
tk.Label(window,text='p',fg='red').pack(side='right')

tk.Label(window,text='P1',font=('Arial',20)).place(x=50,y=100,anchor='nw')

window.mainloop()   #主窗口循环显示






































'''创建一个简单的窗口'''
# Label(text='Spam').pack()
# mainloop()

'''窗口中添加按钮'''
# def reply():
    # showinfo(title='popup',message='Button pressed')
# window = Tk()                                           #k是小写
# button = Button(window,text='press',command=reply)
# button.pack()
# window.mainloop()

'''Frame控件,和上面的例子相同的结果'''

# class MyGui(Frame):
    # def __init__(self,parent=None):
        # Frame.__init__(self,parent)
        # button = Button(self,text='press',command=self.reply)
        # button.pack()
    # def reply(self):
        # showinfo(title='popup',message='Button pressed')

# if __name__ == "__main__":
    # window=MyGui()
    # window.pack()
    # window.mainloop()

'''数据库存储GUI'''
# def reply(name):
    # showinfo(title='Reply',message='Hello'.format(name))
    
# top = Tk()
# top.title('Echo')
# top.iconbitmap('py-blue-trans-out.ico')

# Label(top,text="Enter your name:").pack(side=TOP)
# ent = Entry(top)
# ent.pack(side=TOP)
# btn = Button(top,text="Submit",command=(lambda:reply(ent.get())))
# btn.pack(side=LEFT)
# top.mainloop()



