# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
import re
from hashlib import md5

class translator:
    # Set your own appid/appkey.
    appid = '20221209001490719'
    appkey = 'c9_rADASzdYfvSZNFCDu'

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'zh'
    to_lang =  'en'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    reg = re.compile(r"^[a-zA-Z\d\.\,:\(\)\s]+$1",re.MULTILINE)

    def allEnglish(self,words):
        if(re.match(self.reg,words)!=None):
            return True
        return False

    def translate(self, query):
        if(query==None or query.strip()==""):
            return query
        query = filterChinesepunctuation(query)
        if(self.allEnglish(query)):
            return query

        salt = random.randint(32768, 65536)
        sign = make_md5(self.appid + query + str(salt) + self.appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': self.appid, 'q': query, 'from': self.from_lang, 'to': self.to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(self.url, params=payload, headers=headers)
        result = r.json()["trans_result"][0]["dst"]

        # Show response
        return result

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()



def filterChinesepunctuation(words):
    words = words.replace('，', ',')
    words = words.replace('。', '.')
    words = words.replace('“', '"')
    words = words.replace('”', '"')
    words = words.replace('‘', '\'')
    words = words.replace('’', '\'')
    words = words.replace('、', '\\')
    words = words.replace('（', '(')
    words = words.replace('）', ')')
    return words


if __name__=='__main__':
    transServ = translator()
    print(transServ.translate("你好 peter"))
