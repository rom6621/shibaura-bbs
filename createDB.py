# このファイルはデータベース作成時のみ実行してください
import sqlite3, os

dbname = 'BBS.db'

if os.path.exists(dbname):
    os.remove(dbname)

conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('CREATE TABLE User(id STRING PRIMARY KEY, mailAddress STRING, name STRING)')
cur.execute('CREATE TABLE Thread(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, details STRING)')
cur.execute('CREATE TABLE Entry(id INTEGER PRIMARY KEY AUTOINCREMENT, threadId INTEGER, auther STRING, content STRING)')

cur.close()
conn.commit()
conn.close()