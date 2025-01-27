import urllib.request
import urllib.parse

def main():
    url = 'https://read.qidian.com/chapter/JKeGiyZJtgUsmgY_yC2imA2/'
    # https: // read.qidian.com / chapter / JKeGiyZJtgUsmgY_yC2imA2 / JPa94E2VpPdp4rPq4Fd4KQ2
    start_page = int(input('Input the start page:'))
    end_page = int(input('Input the end page:'))
    for page in range(start_page,end_page):
        #根据url和page去生成指定的request
        request = handle_request(url,page)

def if __name__ == '__main__':


https://read.qidian.com/chapter/JKeGiyZJtgUsmgY_yC2imA2/JPa94E2VpPdp4rPq4Fd4KQ2
https://read.qidian.com/chapter/JKeGiyZJtgUsmgY_yC2imA2/xZ7Hi_Loaq5Ms5iq0oQwLQ2