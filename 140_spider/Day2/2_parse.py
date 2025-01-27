#!/usr/bin/env python3
import urllib.parse

image_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1585567860634&di=bddfb991d1cf4ec2b725b4b7f05a8fbf&imgtype=0&src=http%3A%2F%2F00.minipic.eastday.com%2F20170221%2F20170221212912_cbff414ccd6113e1d49401b874e438c6_9.jpeg'


data = {
    'name':'二狗',
    'age': 'age',
    'sex': '男',
    'height': 'height',
    'weight': 180
}

query_string = urllib.parse.urlencode(data)     #需要传入的参数需要是字典，不仅可以拼接，并且实现了编码(将字典里的中文转换成字符)；
print(query_string)


