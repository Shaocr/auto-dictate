import sqlite3
from config import is_auto_translate
from spider import youdao_spider
class Database(object):
    def connect(self):
        #创建数据库
        self.conn = sqlite3.connect('words.db')
        #游标
        self.c = self.conn.cursor()
        #判断是否连接
        self.is_connect=True
        #判断是否自动翻译
        self.auto_translate = is_auto_translate
        if self.auto_translate:
            self.youdao_translate = youdao_spider()
    #创建表
    def create_table(self):
        assert self.is_connect
        #判断表是否存在
        self.c.execute(
            '''select name from sqlite_master where type='table' order by name
            ''')
        if_exist = self.c.fetchall()
        if if_exist==None:
            # 创建表
            self.c.execute('''CREATE TABLE words_dict
                  (word text primary key, translate text)''')
            print('创建成功')
    def save(self):
        assert self.is_connect
        # 保存操作
        self.conn.commit()
    def close(self):
        assert self.is_connect
        # 关闭连接
        self.conn.close()
        #标记断开连接
        self.is_connect=False
    def save_and_close(self):
        assert self.is_connect
        # 保存操作
        self.conn.commit()
        # 关闭连接
        self.conn.close()
        # 标记断开连接
        self.is_connect=False
    #删除表
    def drop_table(self,table_name):
        assert self.is_connect
        self.c.execute('''drop table %s'''%(table_name))
        print('成功删除')
    #插入单词
    def insert_word(self,word,translate=''):
        assert self.is_connect
        #检测是否已经存在
        self.c.execute('''select * from words_dict where word = ?''',[word])
        if self.auto_translate:
            translates = self.youdao_translate.get_word_translate(word)
        else:
            translates = translate
        if self.c.fetchall()==None:
            self.c.execute(
                '''insert into words_dict values(?,?)''',[word,translates]
            )
        else:
            self.update_word(word,translate)
    #更新单词释义
    def update_word(self,word,translate):
        assert self.is_connect
        self.c.execute(
            '''update words_dict set word = ?,translate=? where word = ?''',[word,translate,word]
        )
    #获取固定单词及释义
    def get_word(self,word):
        assert self.is_connect
        self.c.execute('''select * from words_dict where word=?''',[word])
        words = self.c.fetchall()
        return words
    #获取所有的单词
    def get_all_words(self):
        assert self.is_connect
        self.c.execute('''select * from words_dict''')
        words = self.c.fetchall()
        return words
    #删除固定单词
    def delete_word(self,word):
        assert self.is_connect
        self.c.execute('''delete table words_dict where word=?''',[word])
    #删除所有单词
    def delete_all_word(self):
        assert self.is_connect
        self.c.execute('''delete table words_dict''')
    #导入文件读取单词
    def get_word_num(self):
        assert self.is_connect
        self.c.execute('''select count(word) from words_dict order by word''')
        num=self.c.fetchone()
        return num[0]
    def read_file(self,path):
        with open (path,'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    if is_auto_translate:
                        translates = f.readline()
                        self.insert_word(line,translates)
                    else:
                        self.insert_word(line)

# sqls = Database()
# sqls.connect()
# sqls.insert_word('degrade','贬低')
# sqls.get_word('degrade')
# sqls.save_and_close()
sqls = Database()
