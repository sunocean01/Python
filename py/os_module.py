import os


'''os.access(path, mode):路径权限检查'''
'''
path -- 要用来检测是否有访问权限的路径。
mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
    os.F_OK: 作为access()的mode参数，测试path是否存在。
    os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
    os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
    os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
'''
# ret = os.access(r'./__pycache__',mode=os.X_OK)         #注意是'\';
# ------------------------------------
'''os.chdir(path): 用于改变当前工作目录到指定的路径。'''
# ret = os.getcwd()         #查看当前的工作目录
# os.chdir('./__pycache__')   
# ret = os.getcwd()
# -----------------------------------
'''os.chmod(path,mode): 方法用于更改文件或目录的权限。右键\属性\安全\...'''
'''
path -- 文件名路径或目录路径。
flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
    stat.S_IXOTH: 其他用户有执行权0o001
    stat.S_IWOTH: 其他用户有写权限0o002
    stat.S_IROTH: 其他用户有读权限0o004
    stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
    stat.S_IXGRP: 组用户有执行权限0o010
    stat.S_IWGRP: 组用户有写权限0o020
    stat.S_IRGRP: 组用户有读权限0o040
    stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
    stat.S_IXUSR: 拥有者具有执行权限0o100
    stat.S_IWUSR: 拥有者具有写权限0o200
    stat.S_IRUSR: 拥有者具有读权限0o400
    stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
    stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
    stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
    stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
    stat.S_IREAD: windows下设为只读
    stat.S_IWRITE: windows下取消只读
'''
# os.chmod("/tmp/foo.txt", stat.S_IXGRP)
# ---------------------
'''os.getcwd() 方法用于返回当前工作目录。'''
# ret = os.getcwd()
# --------------------------

'''os.link(src, dst):创建硬链接'''
'''
1，软链接可以理解成快捷方式。它和windows下的快捷方式的作用是一样的。
2，硬链接等于cp -p 加 同步更新。
3、限制不同
    硬链接只能对已存在的文件进行创建，不能交叉文件系统进行硬链接的创建；
    软链接可对不存在的文件或目录创建软链接；可交叉文件系统；
src -- 用于创建硬连接的源地址
dst -- 用于创建硬连接的目标地址
''' 
# existing_filepath = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\140_pyscript\test\test.txt'
# shortcut_path = r'C:\Users\osun\Desktop\test2.txt'
# os.link(existing_filepath,shortcut_path)
# ----------------------------------
'''os.symlink(src, dst):创建一个软链接,windows下创建的链接打不开'''
'''
src -- 源地址。
dst -- 目标地址。
'''
# os.symlink(r'tst.txt',r'C:\Users\osun\Desktop')
'''os.listdir(path):返回指定的文件夹包含的文件或文件夹的名字的列表'''
# ret = os.listdir(r'./')
# -----------------------------
'''os.stat(path):用于在给定的路径(文件夹\文件)上执行一个系统 stat 的调用。'''
'''
stat 结构:
    st_mode: inode 保护模式
    st_ino: inode 节点号。
    st_dev: inode 驻留的设备。
    st_nlink: inode 的链接数。
    st_uid: 所有者的用户ID。
    st_gid: 所有者的组ID。
    st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
    st_atime: 上次访问的时间。
    st_mtime: 最后一次修改的时间。
    st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''
# ret = os.stat(os.getcwd())
# ret = os.stat(r'./test2.txt')
# --------------------
'''os.lstat(path):返回文件的相关信息,像stat(),但是没有软链接'''
# ret = os.lstat(r'./re_module.py')
# ----------------------------------
'''os.mkdir(path, mode=0o777):用于递归创建一级目录'''
'''
path --需要递归创建的目录，可以是相对或者绝对路径。。
mode -- 权限模式。
'''
# os.mkdir(r'./testfolder1')              #好像'/','\'都可以

'''os.makedirs(path, mode=0o777):用于递归创建目录,可用是多级新目录,如果是一级同mkdir'''
'''
path --需要递归创建的目录，可以是相对或者绝对路径。。
mode -- 权限模式。
'''
# os.makedirs(r'./testfolder1/testfolder2/testfolder3/testfolder4')
# -------------------------------
'''os.remove(path):删除指定路径的文件'''
# os.remove("./test.txt")
# ---------------------------
'''os.rmdir(path):删除指定路径的目录,只能是空文件夹'''
# os.rmdir(r'./testfolder1')
# ------------------------------------
'''os.removedirs(path):递归删除目录。像rmdir(),如果子文件夹成功删除,removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。'''
# os.removedirs(r'./testfolder1/testfolder2/testfolder3/testfolder4')
# ----------------------------------
'''os.rename(src,dst):命名(修改)文件或目录，从src到dst,如果dst是一个存在的目录,将抛出OSError。'''
'''
src -- 要修改的目录名(要修改的文件名/文件夹名)
dst -- 修改后的目录名(修改后的文件名/文件夹名)
'''
# ret = os.listdir(os.getcwd())                 #获取当前文件夹下的文件及文件夹
# os.rename('testfolder1','testfolder1_new')
# --------------------------------
'''os.unlink(path):用于删除文件,如果文件是一个目录则返回一个错误。需要在管理员权限下'''
# os.unlink(r'./test2.txt')
# ---------------------------------
'''os.utime(path, times):用于设置指定路径文件最后的修改和访问时间。'''
'''
path -- 文件路径
times -- 如果时间是 None, 则文件的访问和修改设为当前时间,否则, 时间是一个2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。
'''
# os.utime(r'./test.txt',(1330712280, 1330712292))
# ret = os.stat(r'./test.txt')
# -------------------------------------
'''os.walk(top[,topdown=True[,onerror=None[,followlinks=False]]]):通过在目录树中游走输出在目录中的文件名，向上或者向下'''
'''
top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。
'''
# for root,dir,files in os.walk(r'./'):
    # print(root,dir,files,sep='\n')
    # for file in files:
        # print(file)
# ---------------------------------

# exit()

print(ret)