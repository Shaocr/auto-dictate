from tkinter import DISABLED
import tkinter
from listening import thread_start
from config import is_auto_translate,change_is_random
from database import Database
from tkinter.filedialog import askopenfilename
#启动窗口后直接连接数据库
sqls = Database()
sqls.connect()
def link():
    global sqls
    input_word=word.get()
    input_translate = translate.get()
    sqls.insert_word(input_word,input_translate)

def selectPath():
    path_ = askopenfilename()
    str_path.set(path_)

top = tkinter.Tk()
top.title('单词管理系统')

#单词输入框
label_word = tkinter.Label(top,text='单词:')
word = tkinter.StringVar()
enter_word = tkinter.Entry(top,textvariable=word)
label_word.grid(column=0,row=0)
enter_word.grid(column=1,row=0)
#释义输入框
label_translate = tkinter.Label(top,text='释义:')
translate = tkinter.StringVar()
enter_translate = tkinter.Entry(top,textvariable=translate)
label_translate.grid(column=0,row=1)
enter_translate.grid(column=1,row=1)
if is_auto_translate:
    enter_translate.config(state=DISABLED)
#添加单词按钮
insert_value_button=tkinter.Button(top,text='添加单词',command=link)
insert_value_button.grid(column=2,row=0)
#选择文件
label_path = tkinter.Label(top,text='路径:').grid(column=0,row=2)
str_path = tkinter.StringVar()
enter_path = tkinter.Entry(top,textvariable = str_path).grid(column=1,row=2)
path_button = tkinter.Button(top,text='选择文件',command=selectPath).grid(column=2,row=1)
#导入文件
import_button = tkinter.Button(top,text='导入文件').grid(column=2,row=2)

#是否随机听写
random_button = tkinter.Checkbutton(top,text='随机听写',command=change_is_random).grid(column=0,row=3)
#听写按钮
listening_button = tkinter.Button(top,text='开始听写',command=thread_start)
listening_button.grid(column=1,row=3)
# 进入消息循环
top.mainloop()
sqls.save_and_close()