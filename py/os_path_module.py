import os
import glob
import datetime

'''os.path 模块主要用于获取文件的属性。'''

'''os.path.abspath(path):获取文件的绝对路径'''
# ret = os.path.abspath(r'./test.txt')
# -----------------------------------
'''os.path.basename(path):返回文件名'''
# ret = os.path.basename(r'C:\Users\osun\Desktop\Python\Function\library\test.txt')
# ---------------------------------------
'''os.path.commonprefix(list): 返回list(多个路径)中，所有path共有的最长的路径'''
# file_path = glob.glob(r'C:\Users\osun\Desktop\Python\Function\*')
# ret = os.path.commonprefix(file_path)
# ------------------------------
'''os.path.dirname(path):返回文件路径'''
# ret = os.path.dirname(r'C:\Users\osun\Desktop\Python\Function\library\test.txt')
# -----------------------------------
'''os.path.exists(path):判断路径(文件夹或文件)是否存在,存在:True,不存在:False'''
# ret = os.path.exists(r'./test/test.txt')
# ---------------------------------
'''os.path.getatime(path):返回最近访问的时间(浮点型秒数)'''
# ret = os.path.getatime(r'./rw.csv')         #返回的是时间戳
# dt = datetime.datetime.fromtimestamp(ret)
# print(dt)
# -----------------------------------------
'''os.path.getmtime(path):返回文件的最近修改时间'''
# ret = os.path.getmtime(r'./test.txt')
# --------------------------------------
'''os.path.getctime(path):返回文件的创建时间(时间戳)'''
# ret = os.path.getctime(r'./write.csv')
# ----------------------------------
'''os.path.getsize(path):返回文件的大小,如果文件不存在返回错误'''
# ret = os.path.getsize(r'./test.txt')
# ----------------------------
'''os.path.isabs(path):判断路径是否位绝对路径'''
# ret = os.path.isabs(r'./test.txt')
# -----------------------------------
'''os.path.isfile(path):判断路径是否为文件'''
# ret = os.path.isfile(r'./test.txt')
# --------------------------------
'''os.path.isdir(path):判断路径是否为目录'''
# ret = os.path.isdir(r'C:\Users\osun\Desktop\Python\Function')
# ----------------------------
'''os.path.islink(path):判断路径是否为链接,不确定windows适用'''
# ret = os.path.islink(r'C:\Users\osun\Desktop\pythonw.exe')
# ------------------------------
'''os.path.join(path1[, path2[, ...]]):把目录和文件名合并成一个路径'''
# ret = os.path.join(r'C:\Users\osun\Desktop\Python\Function\library',r'test.txt')
# -----------------------------------------
'''os.path.normcase(path):转换path的大小写和斜杠'''
# ret = os.path.normcase(r'C:\Users/osun\\Desktop\\Python\Function\library')
# ----------------------------------------
'''os.path.normpath(path):规范path字符串形式,就是帮你纠错,和normcase有点像'''
# ret = os.path.normpath(r'C:\Users/osun\\Desktop\\\\Python\Function\library')
# ---------------------------
'''os.path.relpath(path[, start]):从start开始计算相对路径'''
# ret = os.path.relpath(r'C:\Users\osun\Desktop\Python\Function\library\test.txt','Desktop')
# relpath = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# ret = os.path.relpath(relpath,'30_Process')
# -------------------------------------
'''os.path.samefile(path1, path2):判断两个目录是否相同,前提条件是两个目录都存在'''
# path1 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# path2 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# ret = os.path.samefile(path1,path2)
# -------------------------------------
'''os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组'''
# path1 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# ret = os.path.split(path1)
# ------------------------------
'''os.path.splitdrive(path):一般用在 windows 下，返回驱动器名和路径组成的元组'''
# path1 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# ret = os.path.splitdrive(path1)
# ------------------------------------
'''os.path.splitext(path):分割路径，返回路径名和文件扩展名的元组'''
# path1 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
# ret = os.path.splitext(os.path.basename(path1))
# ----------------------------
'''os.path.splitunc(path):把路径分割为加载点与文件'''
path1 = r'C:\Users\osun\Desktop\Sensirion\10_Product\60_PM25\100_common\30_Process\50_Machine\3.000.228_MC03_68_20200812-060443-724.edf'
ret = os.path.splitunc(path1)
# -------------------------




print(ret)