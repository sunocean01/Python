'''需要共外部输入三个参数,可以通过如下方法实现:
1. sys.argv[]
2. argparse 类
3. click
'''

import sys
import argparse

# 测试函数,year,name,body三个参数需要从外部输入
def test_for_sys(year,name,body):
    print('this year is:',year)
    print('this name is:',name)
    print('this body is:',body)

'''方法一: sys.argv[]'''

# year,name,body = sys.argv[1:4]



'''方法二:argparse类
使用步骤:
（1）import argparse 首先导入模块
（2）parser = argparse.ArgumentParser（） 创建一个解析对象
（3）parser.add_argument() 向该对象中添加你要关注的命令行参数和选项
（4）parser.parse_args() 进行解析,一个字典
'''

# 需要从外部输入如下三个参数,可以通过argparse类进行输入
# parser = argparse.ArgumentParser(description='Test for argparse')   #对参数实例化
# parser.add_argument('--name','-n',help='name属性,非必要参数')          #添加参数
# parser.add_argument('--year','-y',help='year属性,非必要参数')
# parser.add_argument('--info','-b',help='info属性,非必要参数')
# args = parser.parse_args()                                          #将所有参数收集到字典中



'''方法三:click库,使用装饰器方式,在调用函数时不需要输入参数'''

if __name__ == '__main__':

    # try:
        # test_for_sys(year,name,body)         #args是个字典,year,name,info是key,传入的参数是值;
    # except Exception as e:
        # print(e)
    # exit()
# ----------------------------------------
    try:
        test_for_sys(args.year,args.name,args.info)         #args是个字典,year,name,info是key,传入的参数是值;
    except Exception as e:
        print(e)
    
r'''
在命令行如下输入:
C:\Users\osun\Desktop\Python\Function\library>python argparse_module.py -n Lyli -y 2021 -b "How are you!"
this year is: 2021
this name is: Lyli
this body is: How are you!
'''