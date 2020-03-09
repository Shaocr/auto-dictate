from database import *
from spider import *
import os
from time import sleep
from config import listening_interval
from playsound import playsound
import random
import threading
db = Database()
db.connect()
sp = youdao_spider(1)

def start_listening():
    from config import is_random
    #连接数据库
    db.connect()
    #获取所有单词数目
    words = db.get_all_words()
    num_word = db.get_word_num()
    #随机播放
    if is_random:
        playList = random.sample(range(0,num_word), num_word)
    else:
        playList = range(0,num_word)
    #顺序播放
    for i in playList:
        str_word = words[i][0]
        filename = 'audios/'+str_word+'.mp3'
        #存在本地音频就播放
        if os.path.exists(filename):
            playsound(filename)
        #不存在就去下载
        else:
            sp.get_word_audio(str_word)
            playsound(filename)
        sleep(listening_interval)
    #关闭数据库
    db.close()
t1 = threading.Thread(target=start_listening)
def thread_start():
    t1.setDaemon(True)
    t1.start()

