import optparse

'''optparse主要为脚本传递命令参数'''

usage = r"python %prog -u/--user <target user> -p/--password <target password>"
parser = optparse.OptionParser(usage)   #写入上面的帮助信息
parser.add_option('-u','--user',type='string',help='target user',default='root')
parser.add_option('-p','--password',type='string',help='target password')
options,args = parser.parse_args()
print('options:',options)
print('ID:',options.user)
print('password:',options.password)
print('args:',args)

r'''
C:\..\library>python optparse_module.py -u OSUN -p 12345
options: {'user': 'OSUN', 'password': '12345'}
ID: OSUN
password: 12345
args: []

C:\..\library>python optparse_module.py -u OSUN -p 12345 s343y
options: {'user': 'OSUN', 'password': '12345'}
ID: OSUN
password: 12345
args: ['s343y']
'''

