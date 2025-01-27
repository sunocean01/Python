#!/usr/bin/env python3

import urllib.request

url = 'http://www.baidu.com'

# image_url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1564154457,2160326790&fm=26&gp=0.jpg'

'''
完整的url：
http://www.baidu.com:80/index.html?name=goudan&password=123#lala
其中':80'可以省略，是默认的
'''

# 获取url请求的响应对象
# response = urllib.request.urlopen(url)
# response = urllib.request.urlopen(image_url)
#
# #response 返回的是对象，对对象进行解读的函数有：
# #1. read()   读取响应内容
# print(response.read())     #读取出来的内容是字节格式，开头有个b，如果是图片就只能以二进制格式写入本地
# print(response.read().decode())    #将读出来的字节格式转化成字符串格式，默认是utf8，是否选gbk，根据网页中使用的编码方式
#
# # 2. geturl()  根据响应内容获取请求的url
# print(response.geturl())
#
# # 3. getheaders()   #获取头部信息，类型:列表里面套元组；
# print(response.getheaders())
#
# # 4. getcode()  #获取状态码
# print(response.getcode())
#
# # 5. readlines()    #按行读取内容，返回列表，都是字节类型
# print(response.readlines())



#将响应内容写入本地

#方法1：常规写入方式：
# with open('image.jpg','wb') as fp:
#         fp.write(response.read())

#方法2：直接将响应的内容写入本地
urllib.request.urlretrieve(url,'bu.txt')



