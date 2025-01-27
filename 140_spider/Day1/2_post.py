import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

word = input('Input the word:')

form_data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '468960.246993',
    'token': '63ddcc6be16025141a02494cc49071b8',
    'domain': 'common',
}

headers = {
    'authority': 'fanyi.baidu.com',
    'method': 'POST',
    'path': '/v2transapi?from=en&to=zh',
    'scheme': 'https',
    'accept': '* / *',
    # 'accept - encoding': 'gzip, deflate, br',
    'accept - language': 'en - US, en;q = 0.9',
    # 'content - length': '133',
    # 'content - type': 'application / x - www - form - urlencoded;',
    # 'charset' = 'UTF - 8',
    'cookie': 'BIDUPSID=DEFB3DC0EA0E6BDDC3092CAF3F0059D8; PSTM=1540785413; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BAIDUID=D3B839AE82B2A7CD04501FD3F09DFF13:FG=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; MCITY=-289%3A; H_PS_PSSID=30971_1462_31169_21098_31187_31217_30823_26350_31164_31195; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1584429090,1584771197,1585022401,1586133543; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1586133543; __yjsv5_shitong=1.0_7_566d4a7396cdcea3883eb779806cd6061493_300_1586133546378_183.192.23.251_579b90ae; yjs_js_security_passport=6036c94e1b8febb7e2551cf8609ca61dfd45a665_1586133546_js',
    'origin': 'https: // fanyi.baidu.com',
    'referer': 'https: // fanyi.baidu.com /',
    'sec - fetch - dest': 'empty',
    'sec - fetch - mode': 'cors',
    'sec - fetch - site': 'same - origin',
    'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    # 'x - requested -with': 'XMLHttpRequest',
}


request = urllib.request.Request(url=post_url,headers=headers)

form_data = urllib.parse.urlencode(form_data).encode()

responese = urllib.request.urlopen(request,form_data)

print(responese.read().decode())



