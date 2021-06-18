# このファイルはデータベース作成時のみ実行してください
import sqlite3, os

dbname = 'test.db'

if os.path.exists(dbname):
    os.remove(dbname)

conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('CREATE TABLE User(id STRING PRIMARY KEY, mailAddress STRING)')
cur.execute('CREATE TABLE Thread(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, details STRING)')
cur.execute('CREATE TABLE Entry(id INTEGER PRIMARY KEY AUTOINCREMENT, threadId INTEGER, auther STRING, content STRING)')

cur.execute('INSERT INTO User(id, mailAddress) values("al00000", "al00000@shibaura-it.ac.jp")')
cur.execute('INSERT INTO Thread(name, details) values("テストスレッド", "テストの内容です")')
cur.execute('INSERT INTO Entry(threadID, auther, content) values(1, "al00000", "テストの書込です")')

conn.commit()
conn.close()