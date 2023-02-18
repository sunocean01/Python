import xml.etree.ElementTree as ET
import xml.dom.minidom as dm
from lxml import etree
import lxml
from bs4 import BeautifulSoup

#XML文件的读取
xml_path = r".\testfile\test.xml"
# tree = ET.ElementTree(file=xml_path)                     #方法一:获取xml文件的树,没有xpath
# tree = ET.parse(xml_path)             #同方法一,没有xpath
tree = etree.parse(xml_path)            #有xpath
# tree_dm = dm.parse(xml_path)            #xml.dom.minidom 方法

'''方法一:ElementTree:迭代/iter()/(find/findall/iterfind)'''
def ElementTree_for():
    root = tree.getroot()                               #获取树的根,根也是元素,元素就可以有属性
    tag = root.tag                                      #获取元素的标签(标记)
    attrib = root.attrib                                #获取元素的属性

    #遍历根元素下面的子元素,及对子元素中的元素再次进行遍历
    for child in root:
        child_tag = child.tag
        child_attrib = child.attrib['id']             #获取子元素中的属性或者属性的值(如果有该属性)
        text = child.text                               #获取元素中的内容
        print(child_tag,child_attrib,text,sep='\n')
        for sub_child in child:
            print(sub_child.tag,sub_child.attrib)
    # 还可以通过索引值来访问特定的元素
    # subtag = root[1].tag
    # subattrib = root[1].attrib
    # print(subtag,subattrib)
    # print('='*40,'end','='*40,sep='')
# ElementTree_for()


def ElementTree_iter_parsing():
    # root = tree.getroot()
    
    #对包括根元素进行遍历
    # for elem in tree.iter():                    #也可以对某个特定的元素对象进行遍历
        # print(elem.tag,elem.attrib,elem.text)
    #对指定的条件进行遍历
    # for elem in tree.iter(tag='book'):
        # print(elem.tag,elem.attrib,elem.text)
    #对指定的元素进行遍历
    # for elem in root[1][1]:
        # print(elem.tag,elem.attrib)
    print('='*40,'end','='*40,sep='')
# ElementTree_iter_parsing()

def ElementTree_path_parsing():
    # find: 找出第一个匹配的子元素;
    # findall: 以列表形式返回所有匹配的子元素
    # iterfind:返回所有匹配元素的迭代器
    '''这三个函数支持部分xpath路径选择的方法'''
    
    #'.' 选取当前节点(根节点bookstore)
    # select_Eelem = tree.findall(r'.')
    
    #'/' 选取子节点
    # select_Eelem = tree.findall(r'./')            #遍历bookstore下一级的所有节点
    # select_Eelem = tree.findall(r'./history')   #遍历bookstore下面的所有标签名为history的节点
    # select_Eelem = tree.findall(r'./history/')   #两个(所有)history,遍历每一个history下面的所有
    # select_Eelem = tree.findall(r'./history/book')   #遍历history下一级标签为book的所有元素
    
    #'//' 遍历当前节点下的所有元素,不分位置层级
    # select_Eelem = tree.findall(r'.//')         #遍历根目录bookstore下的所有目录
    # select_Eelem = tree.findall(r'.//book')     #遍历根目录下所有标签为book的元素
    # select_Eelem = tree.findall(r'./history//book')     #遍历所有history下的标签为book的所有元素
    select_Eelem = tree.findall(r'./history[1]//book')     #遍历第一个history下的标签为book的所有元素
    # select_Eelem = tree.findall(r'./history[last()]//book')     #遍历最后一个history下的标签为book的所有元素
    # select_Eelem = tree.findall(r'./history[last()-1]//book')     #遍历倒数第二个history下的标签为book的所有元素
    
    #'@' 选取属性
    #谓语:谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中。
    # select_Eelem = tree.findall(r'./political/book[@country]')       #遍历所有带有contry属性的元素
    # select_Eelem = tree.findall(r'./political/book[@country="China"]')       #遍历所有带有contry="China"属性的元素
    
    print(select_Eelem)
    for elem in select_Eelem:
        print(elem.tag,elem.attrib,elem.text)
    print('='*40,'end','='*40,sep='')
# ElementTree_path_parsing()


'''方法二:xpath'''
def xpath_parsing():
    '''定位'''
    ''' '.':选取当前节点'''
    # select_Eelem = tree.xpath(r'.')
    
    ''' './':从根节点选取'''
    # select_Eelem = tree.xpath(r'/bookstore/*')        #选取根节点(bookstore)下面所有的子节点
    # select_Eelem = tree.xpath(r'./*')                 #同上一条
    # select_Eelem = tree.xpath(r'/bookstore/history')    #选取bookstore下面的所有的history节点
    
    ''' '//': 在所有层级节点中查找'''
    # select_Eelem = tree.xpath(r'.//book/*')
    
    ''' '..':选择当前节点的父节点'''
    # select_Eelem = tree.xpath(r'/bookstore/history/book/..')  #就是向上一级,是history
    
    '''谓语:谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中。'''
    # select_Eelem = tree.xpath(r'./history[1]')          #选择第一个history
    # select_Eelem = tree.xpath(r'./history[last()]')          #选择第最后一个history
    # select_Eelem = tree.xpath(r'./history[1]/book[last()-1]')          #选择第第一个history下面的倒数第二个book元素
    # select_Eelem = tree.xpath(r'./history/book[1<position()<4]')          #共有5(3+2)个book,取位置是2~3的book
    # select_Eelem = tree.xpath(r'./history/book[@country]')          #取有country属性的book, xml里一个元素下面如果同时有子元素和内容,内容要放在最前面;
    # select_Eelem = tree.xpath(r'./history/book[@country="China"]')          #将country属性值是"China"的取出来
    
    '''模糊匹配定位:contains(字符串查找函数):包含xxx; starts-with(字符串查找函数):开头是xxx'''
    # select_Eelem = tree.xpath(r'./history/book[contains(@country,"i")]')          #country属性值里面包含'i'的取出来
    # select_Eelem = tree.xpath(r'./history/book[starts-with(@country,"A")]')          #将country属性值开头是'A'的取出来

    '''运算符定位'''
    # select_Eelem = tree.xpath(r'./history/book[price>29]')          #按照子元素的条件查找
    # select_Eelem = tree.xpath(r'./history/book[price<10 or price>30]')          #按照子元素的条件查找
    # select_Eelem = tree.xpath(r'./history/book[price>29]//price')          #接着上面的条件继续往下查所有price子元素
    '''xpath中可有+,-,*,div,=(等于),!=,<,>,<=,>=,or,and,mod(计算除法余数)'''

    '''选取未知节点'''
    #'*':匹配任何元素节点
    # select_Eelem = tree.xpath(r'./history/*')             #查找history下一级的所有元素节点
    # select_Eelem = tree.xpath(r'./history//*')             #查找history下面的所有元素节点,不分层级
    # select_Eelem = tree.xpath(r'./history/tag[@*]')             #查找所有带有属性的tag元素
    
    ''' '|':选取若干路径'''
    # select_Eelem = tree.xpath(r'./history/magzine | ./nature')          #使查找更间接灵活
    
    '''取值'''
    '''@:取属性'''
    # select_Eelem = tree.xpath(r'./history/@*')          #返回列表: 所有history的所有属性值
    # select_Eelem = tree.xpath(r'./history/book[1]/@country')       #返回列表,取属性country属性的值,取每个history下面的第一个book的country的值
    
    '''text():取文本'''
    select_Eelem = tree.xpath(r'./history[1]/book/text()')              #包括换行符和空格
    # select_Eelem = tree.xpath(r'./history[1]/book[1]/text()')              #包括换行符和空格
    
    '''tag/attrib/text:取标签,属性,文本'''
    # select_Eelem = tree.xpath(r'./history[1]/book[1]')              #包括换行符和空格
    # print(select_Eelem[0].tag,select_Eelem[0].attrib,select_Eelem[0].text)      #注:xpath返回的是列表,所以要先取元素

    print(select_Eelem)
    # for elem in select_Eelem:
        # print(elem.tag,elem.attrib,elem.text)
xpath_parsing()


'''方法三:xml.dom'''
def dom_parsing():
    '''documentElement:获取xml文档对象'''
    root = tree_dm.documentElement
    
    '''childNodes:获取二级节点列表'''
    # sec_childs_lt = root.childNodes
    # print(sec_childs_lt)
    # exit()
    
    '''getElementsByTagName('tagname'):根据标签名直接查找'''
    elem_list = root.getElementsByTagName('history')
    for elem in elem_list:
        print(elem.nodeName,                #获取该标签的名称
                elem.nodeValue,             #获取该标签的值?????
                elem.nodeType,              #获取该标签的类型,见对照表
                elem.firstChild.data,       #获取文本值
                elem.getAttribute('id'),    #获取属性的值,确定是要先知道有哪些属性
                
                elem.attributes['id'],      #返回id属性对象
                elem.attributes['id'].name,    #该属性的key,即'id'
                elem.attributes['id'].value,    #该属性的value,即 elem.getAttribute('id')返回的值
                sep='\n')
# dom_parsing()


'''方法四:bs4'''
def bs4_parsing():
    soup = BeautifulSoup(open(xml_path),'lxml')         #注意:要先打开xml文件
    '''基本方法'''
    # print(
            # soup.history,              #按标签名查找,返回第一个; 以bs4.tag(看上去是文本)形式返回
            # soup.history.attrs,        #获取该节点元素的所有属性的字典
            # soup.history['type'],      #获取指定属性的值
            
            #三种方法查找内容文本
            # soup.history.text,         #查找该节点下的所有文本内容,不分层级;
            # soup.price.string,          #返回节点下的文本内容,仅该节点下没有子节点适用;
            # soup.book.get_text(),     #同text;
            # sep='\n')
    
    '''find 查找,定位以后就可以用上面的基本方法查属性/内容'''
    SoupFind = soup.find('history',type="Antique"),  #返回元组,find方法查找,第二个参数可选:指定节点的属性; 在网页的html文件如果有属性是class="xxx", 这个地方class要写成class_
    child = SoupFind[0].find('book')                #因为SoupFind是元组,所以要取位得到<class 'bs4.element.Tag'>再进行使用find
    # child = SoupFind[0].find()                #什么参数都不给的话,找到的是第一个;
    sub_child = child.find('price')                 #这样就可以一级一级的找下去了
    # print('SoupFind type:{}'.format(type(SoupFind)),sep='\n',end='\n'+'-'*50+'\n')
    # print('SoupFind[0] type:{}'.format(type(SoupFind[0])),sep='\n',end='\n'+'-'*50+'\n')
    # print('SoupFind content:{}'.format(SoupFind),sep='\n',end='\n'+'-'*50+'\n')
    # print('child type:{}'.format(type(child)),sep='\n',end='\n'+'-'*50+'\n')
    # print('child content:{}'.format(child),sep='\n',end='\n'+'-'*50+'\n')
    # print('sub_child content:{}'.format(sub_child),sep='\n',end='\n'+'-'*50+'\n')
    
    '''找到后就可以用上面介绍的基本方法提取对应的内容了'''
    # print(
            # child.attrs,
            # child.attrs['country'],
            # child.text,                 #提取下面所有的文本,部分层级
            # sep='\n',
            # end='\n'+'-'*50+'\n')
    
    '''find_all查找'''
    print(
           # soup.find_all(),                                   #查找所有的标签
           # soup.find_all('book'),                             #查找所有的'book'标签
           # soup.find_all('book',country="China"),             #传入第二个参数,属性限制;
           # soup.find_all('book',country="China",limit=1),     #传入第三个参数,限制查找的次数
           # soup.find_all(['book','magzine']),                 #可以给个列表,同时查找多种的所有标签  
           # soup.find_all(['book','magzine'])[0].find_all(),   #同样所有的<class 'bs4.element.Tag'>,find_all都是适用的
            sep='\n')

# bs4_parsing()


    #这样就可以一级一级的找下去(即去指定的div中查找'a')
# div = soup.find('div', class_="stock_sub")
# print(div.find('a'))
# print(div.select('.stockTable > a'))   #select 也可以通过普通对象来调用，找到对象里面符合要求的搜索对象

#find_all 获取所有股票的href和股票名称
# div = soup.find('div', class_="stock_sub")
# lt = div.find_all('a')
# for href_text in lt:
#     print(href_text['href'])
#     print(href_text.string)
