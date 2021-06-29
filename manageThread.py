#################################################
# Designer :石川公彬
# Date :2021.06.25
# Purpose :スレッドの情報登録と検索処理を行う
#################################################

#################################################
# Function Name :threadRegistration
# Designer :石川公彬
# Date :2021.06.22
# Function:DBにスレッドの名前と詳細を登録し、スレッドIDを抽出し、情報をnewThreadで返す
# Return :newThread
#################################################

import sqlite3
from threading import Thread
import classes
# スレッド情報登録


def threadRegistration(name, details):

    # データベース作成
    conn = sqlite3.connect("test.db")
    # カーソルオブジェクトの作成
    cur = conn.cursor()

    # threadテーブルへスレッド名と詳細の登録
    sql = 'INSERT INTO Thread(name, details) VALUES("' + \
        name + '", "' + details + '")'
    cur.execute(sql)

    # スレッドIDを抽出
    sql = 'SELECT id FROM Thread ORDER BY id DESC LIMIT 1'
    cur.execute(sql)

    newThreadId = cur.fetchone()

    cur.close()
    conn.commit()
    conn.close()

    return newThreadId

#################################################
# Function Name :getThread
# Designer :石川公彬
# Date :2021.06.22
# Function:スレッドIDからDBを検索し、スレッド情報を取得する
# Return :newThread
#################################################

# スレッド情報取得


def getThread(id):

    # データベース作成
    conn = sqlite3.connect("test.db")
    # カーソルオブジェクトの作成
    cur = conn.cursor()

    # スレッドIDを抽出
    sql = 'SELECT * FROM Thread WHERE id="' + str(id) + '"'
    cur.execute(sql)

    # threadにスレッドの情報を入れる
    thread = cur.fetchone()

    cur.close()
    conn.close()

    # newThreadにスレッドの情報を入れる
    return thread

#################################################
# Function Name :search
# Designer : 石川公彬
# Date :　2021/06/25
# Function:　DBからスレッドの情報を検索し、それをresultThreadで返す
# Return :returnThread
#################################################

# スレッド検索


def search(searchKeys):
    searchWords = searchKeys[0]
    searchTags = searchKeys[1]

    resultThreads = []

    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    sql = 'SELECT id FROM Thread'

    # searchWordsとsearchTagsの要素数が0でなければif文に入る
    if (len(searchWords) != 0) or (len(searchTags) != 0):
        sql += ' WHERE'
        # searchWordsの要素数が0でなければif文に入る
        if len(searchWords) != 0:
            for searchWord in searchWords:
                sql += (' name LIKE "%' + searchWord + '%" OR')
                # searchWordをsql文に追加
        # searchTagsの要素数が0でなければif文に入る
        if len(searchTags) != 0:
            for searchTag in searchTags:
                sql += (' tags LIKE "%' + searchTag + '%" OR')
                # searchTagをsql文に追加
         # 右からORを探して見つけたら削除
        sql = sql.rstrip(' OR')

    cur.execute(sql)
    results = cur.fetchall()

    for result in results:
        id = result[0]
        new = classes.Thread.getThread(id)
        # resultThreadにnewThreadを追加
        resultThreads.append(new)

    cur.close()
    conn.close()

    return resultThreads
