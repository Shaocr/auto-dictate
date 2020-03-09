#发音方式 1:英式发音 2:美式发音
pronounce_type = 1
#听写时间间隔
listening_interval=6
#是否开启自动翻译--保存单词时自动有道翻译
is_auto_translate=True
#是否随机听写标志
is_random=False












def change_is_random():
    global is_random
    if is_random:
        is_random=False
    else:
        is_random=True