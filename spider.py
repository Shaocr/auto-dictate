import requests
from lxml import etree
class youdao_spider(object):
    def __init__(self,pronounce_type=1):
        #audio_url 是音频请求请求网址
        self.audio_url = 'http://dict.youdao.com/dictvoice?audio=%s&type=%s'
        #translate_url 是释义请求网址
        self.translate_url = 'http://www.youdao.com/w/eng/%s/#keyfrom=dict2.index'
        self.pronounce_type = str(pronounce_type)
    def get_word_audio(self,word):
        request_url = self.audio_url%(word,self.pronounce_type)
        with requests.get(request_url, stream=True) as r:
            chunk_size = 1024
            with open('audios/'+word+'.mp3', "wb") as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
    def get_word_translate(self,word):
        requests_url = self.translate_url%(word)
        response = requests.get(requests_url)
        html = etree.HTML(response.text)
        translate = html.xpath('//*[@id="phrsListTab"]/div/ul/li')
        res = ''
        for i in translate:
            res+=i.text
        return res
#file  = requests.get('')
a = youdao_spider(1)
#a.get_word_audio('degrade')
a.get_word_translate('degrade')