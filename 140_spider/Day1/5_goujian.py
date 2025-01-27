import urllib.request
import urllib.parse
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context()

url = 'http://www.baidu.com/'

response = urllib.request.urlopen(url)
print(response.read().decode())

#伪装头部
headers = {
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
}

#构建请求对象
request = urllib.request.Request(url=url,headers=headers)

#发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())

