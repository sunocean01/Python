import urllib.request
import urllib.parse

# 创建handler
handler = urllib.request.ProxyHandler({'https':'117.88.177.24:3000'})

#opener

opener = urllib.request.build_opener(handler)


url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=&tn=baidu&bar=&wd=ip&rn=&oq=&rsv_pq=&rsv_t=98b5Wbx7pStTusFLC8thnFj3c4v8BQqwrIZdCAD89Qz9c19RuvnETBQ8HrM&rqlang='

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}


request = urllib.request.Request(url=url,headers=headers)

response = opener.open(request)

with open('ip.html','wb') as fp:
    fp.write(response.read())


