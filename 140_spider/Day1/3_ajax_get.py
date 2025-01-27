import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=80'

page = int(input('Input the page number:'))

#start  limit


number = 20

#构建get参数

data = {
    'start': (page-1)*number,
    'limit': number,
}

#将字典转化为query_string
query_string = urllib.parse.urlencode(data)

#修改url
url += query_string

#
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}


request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())

