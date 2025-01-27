import urllib.request
import urllib.parse
import http.cookiejar
import re

# string = '<p><div><span>猪八戒</span></div></p>'
# pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
# ret = pattern.search(string)
# print(ret)
#
#
#
# string2 = '<div>改进后肉体和</div></div></div>'
# pattern2 = re.compile(r'<div>.*?</div>')
# ret2 = pattern2.search(string2)
# print(ret2)


string2 = ''' hate is a beautiful feel 
love a
love b
love c very much
'''

patter3 = re.compile(r'^love',re.M)

ret3 = patter3.findall(string2)

print(ret3)
