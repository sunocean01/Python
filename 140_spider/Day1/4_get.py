#!/usr/bin/env python3

import urllib.request
import urllib.parse

name = input('Input:')
url = 'https://www.baidu.com/s?'



data = {
    'ie': 'utf-8',
    'name': name,
}

query_string = urllib.parse.urlencode(data)

url += query_string


print(url)

