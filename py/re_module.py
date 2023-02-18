import re

'''re.compile(pattern,flags=0):编译正则表达式模式，返回一个对象的模式。'''
'''
pattern:编译时用的表达式字符串,如: r'.*9E4E1.*'
flag 编译标志位，用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等。常用的flags有：
re.S(DOTALL):使.匹配包括换行在内的所有字符;
re.I(IGNORECASE): 使匹配不区分大小写;
re.L(LOCAL):做本地化识别(local-aware)匹配,语法等;
re.M(MULTILINE):多行匹配,影响^和$;
re.X(VERBOSE):这个标记允许你编写更具可读性更友好的正则表达式。通过分段和添加注释。空白符号会被忽略，除非在一个字符集合当中或者由反斜杠转义，或者在*?,(?:or(?P<…>分组之内。当一个行内有 #不在字符集和转义序列，那么它之后的所有字符都是注释。
re.U:根据Unicode字符集解析字符,这个标志影响\w,\W,\b,\B;
'''
# tt = "Tina is a goOdd girl, she is cool, clever, and so on...\n"
# rr = re.compile(r'\w*oo\w*',re.I)       #r'\w*oo\w*': \w代表所有的字母,数字和_, 不包括空格; 所以返回的是词语;
# zhengze = rr.findall(tt)
# zhengze = re.findall(rr,tt)
# ------------------------------------
#re.X:给正则符合加备注
# tt = "Tina is a goOd girl, she is cool, clever, and so on...\n"
# rr = re.compile(r"""\w*     #可以构成词语的绝大部分字符，也包括数字和下划线
                    # oo      #包含连续的两个o
                    # \w      #尾部同头部""",re.X)
# zhengze = rr.findall(tt)
# -----------------------------------
'''re.search(pattern, string, flags=0):扫描整个字符串并返回第一个成功的匹配的单词'''
'''
pattern:匹配的正则表达式;
string:要匹配的字符串;
flags:标识位;
'''
# tt = "Tina is a goOd girl, she is cool, clever, and so on...\n,Zoo"
# rr = re.compile(r'\w*oo\w',re.I)
# zhengze = rr.search(tt)                 #返回一个对象,包含位置信息,及单词
# zhengze = re.search(rr,tt).span()       #提取对象中的span(),及所查找单词的位置;
# -----------------------------
'''match(pattern,string,flag=0):只从字符串的最头进行匹配，成功返回匹配对象（只有一个结果），否则返回None'''
'''
pattern:匹配的正则表达式;
string:要匹配的字符串;
flags:标识位;
类似字符串方法:startswith(),返回内容不一样;
'''
# tt = "Tina is a goOd girl, she is cool, clever, and so on...\n,Zoo"
# rr = re.compile(r'\w*Tin\w',re.I)
# zhengze = rr.match(tt)                 #返回一个对象,包含位置信息,及单词
# ------------------------------
'''group()/groups(), 该对象又有以下方法'''
'''
. group() 返回被 RE 匹配的字符串
. start() 返回匹配开始的位置
. end() 返回匹配结束的位置
. span() 返回一个元组包含匹配 (开始,结束) 的位置
. group() 返回re整体匹配的字符串，可以一次输入多个组号，对应组号匹配的字符串。
a. group（）返回re整体匹配的字符串，
b. group (n,m) 返回组号为n，m所匹配的字符串，如果组号不存在，则返回indexError异常
c.groups（）groups() 方法返回一个包含正则表达式中所有小组字符串的元组，从 1 到所含的小组号，通常groups()不需要参数，返回一个元组，元组中的元就是正则表达式中定义的组。
'''
tt = "Tina is a goOd girl, she is cool, clever, ggabgitrt and so on...,Zoo,number is 23143abgd56546 test"
# rr = re.compile(r'\w*abg\w',re.I)                       #包含'abg'的所有词语;
rr = re.compile(r"([0-9]+)([a-z]*)(bg)([a-z]*)([0-9]+)",re.S)     #数字+字母+'abg'+字母+数字
# zhengze = rr.search(tt)             #返回对象:<_sre.SRE_Match object; span=(79, 93), match='23143abgd56546'>
# zhengze = rr.search(tt).group()     #返回满足条件的字符串:'23143abgd56546'
# zhengze = rr.search(tt).start()     #返回字符串起点位置:79
# zhengze = rr.search(tt).end()       #返回字符串终点位置:93
# zhengze = rr.search(tt).span()       #返回字符串起点终点位置(10,14)

# zhengze = re.search(rr,tt).group(1)      #返回'23143',对应的第一个位置 ([0-9]+)
# zhengze = rr.search(tt).group(2)         #返回'a',对应的第二个位置的([a-z]*)
# zhengze = re.search(rr,tt).group(3)      #返回'bg',对应的第三个位置的(bg)
# zhengze = re.search(rr,tt).group(4)      #返回'd',对应的第四个位置的([a-z]*)
# zhengze = re.search(rr,tt).group(5)      #返回'56546',对应的第五个位置的([0-9]+)
# zhengze = re.search(rr,tt).groups()      #返回5个位置的元组:('23143', 'a', 'bg', 'd', '56546')
# -----------------------------------
'''findall(pattern, string, flags=0):查找字符串中所有符合条件的字符串,返回列表'''
'''
pattern:匹配的正则表达式;
string:要匹配的字符串;
flags:标识位;
'''
# tt = "Tina is a good girl, she is cool, clever, and so on...\n"
# rr = re.compile(r'\w*oo\w*',re.I)
# zhengze = rr.findall(tt)                             #返回:['good', 'cool']
# zhengze = re.findall(r'(\w)*oo(\w)*',tt)            #返回:[('g', 'd'), ('c', 'l')],()表示子表达式,也可以试着把'oo'改成(oo)
# ------------------------------
'''re.finditer(pattern, string, flags=0): 与findall方法类似,以迭代器形式返回结果'''
# tt = "Tina is a good girl, she is cool, clever, and so on...\n"
# rr = re.compile(r'\w*oo\w*',re.I)
# zhengze = rr.finditer(tt)                             #返回:['good', 'cool']
# ------------------------------
'''re.split(pattern, string[, maxsplit]):按照能够匹配的子串将string分割后返回列表'''
# tt = r"one1two2three3four4five5"
# rr = re.compile(r'\d+')
# rr = re.compile(r'(\d+)')
# zhengze = re.split(rr,tt)
# zhengze = rr.split(tt)
# ------------------------------
'''re.sub(pattern, repl, string, count=0,flaga=0):使用re替换string中每一个匹配的子串后返回替换后的字符串。'''
'''
pattern:正则表达式;
repl: 要替换的内容;可以是字符串,也可以是函数;
string: 目标字符串;
count: 替换次数;默认0即替换所有
flags: 可选,默认0
'''
# tt = "JGood is a handsome boy, he is cool, clever, and so on..."
# rr = re.compile(r'\s+')
# zhengze = re.sub(rr,'-',tt,5)

# re.sub还允许使用函数对匹配项的替换进行复杂的处理。
# 如：re.sub(r'\s', lambda m: '[' + m.group(0) + ']', text, 0)；将字符串中的空格' '替换为'[ ]'。
# ------------------------
'''subn(pattern, repl, string, count=0, flags=0):返回替换后的内容及替换次数'''
# tt = "JGood is a handsome boy, he is cool, clever, and so on..."
# rr = re.compile(r'\s+')
# zhengze = re.subn(rr,'-',tt)

print(zhengze)

