import urllib.request
import urllib.parse


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'



city = input('input the city name:')
page = input('Input the page number:')
size = input("Input the quatity:")
formdata = {
    'cname':  city,
    # 'pid':  ,
    # 'keyword': city,
    'pageIndex': page,
    'pageSize': size,
}


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request,data=formdata)

print(response.read().decode())
