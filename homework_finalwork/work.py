import requests
import json
import sqlite3

def get_data(page):#获取原始用户评论数据
    header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Mobile Safari/537.36'}
    url = "http://m.maoyan.com/review/v2/comments.json?movieId=249342&userId=-1&offset="+str(page)+"&limit=15&ts=1545206997098&type=3"
    html = requests.get(url, headers=header)
    m = html.json()['data']['comments']
    
    for i in range(15):#写入数据库
        a =  m[i]['nick']
        b = m[i]['id']
        c = m[i]['content']
        save_data(a,b,c)

def save_data(a,b,c):#定义写入数据库的函数
    cur.execute('insert into data values(?,?,?)',(a,b,c))

conn = sqlite3.connect("D://data.db")#创建数据库文件
cur = conn.cursor()
cur.execute('create table data(nick varchar(20),id char(10),content varchar(200))')
for n in range(1000): #遍历网页
    get_data(n)
conn.commit()
conn.close()