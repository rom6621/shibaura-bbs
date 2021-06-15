# このファイルはデータベース作成時のみ実行してください

import sqlite3

dbname = 'BBS.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()
cur.execute('CREATE TABLE User(id STRING PRIMARY KEY, mailAddress STRING)')

conn.close()