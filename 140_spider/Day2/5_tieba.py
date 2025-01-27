import urllib.request
import urllib.parse
import os

url = 'https://tieba.baidu.com/f?kw=python&ie=utf-8&'



#输入吧名，输入起始页码，输入结束页码，在当前文件夹中创建以吧名为文件夹，里面是每一页的html的内容，文件名是吧名_page.html

ba_name = input('Input the ba name:')
start_page = int(input('Input the start page:'))
end_page = int(input('Input the end page:'))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)


#循环，依次爬取每一页数据

for page in range(start_page,end_page+1):



    #page 就是当前页
    #拼接url的过程
    data = {
        'kw': ba_name,
        'pn': (page - 1)*50
    }

    data = urllib.parse.urlencode(data)
    url_t = url + data
    # print(url_t)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

    request = urllib.request.Request(url=url_t,headers = headers)

    print('Page {} start loading....'.format(page))

    response = urllib.request.urlopen(request)


    #生产文件名
    filename = ba_name + '_' + str(page) + '.html'
    filepath = ba_name + '/' + filename

    with open(filepath,'wb') as fp:
        fp.write(response.read())

print('Page {} finish loading....'.format(page))