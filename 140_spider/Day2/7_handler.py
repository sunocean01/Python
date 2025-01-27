import urllib.request
import urllib.parse


url = 'https://www.baidu.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

#创建一个handler
handler = urllib.request.HTTPHandler()

#通过handler创建一个opener,opener 就是一个对象，一会发送请求时，直接使用opener里面的方法即可，不要使用urlopen了
opener = urllib.request.build_opener(handler)

#构建请求对象
request = urllib.request.Request(url,headers=headers)


#发送请求
response = opener.open(request)
print(response.read().decode())




