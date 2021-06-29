#################################################
# Designer :石川公彬
# Date :2021.06.25
# Purpose :
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

    conn = sqlite3.connect("test.db")
    # データベース作成
    cur = conn.cursor()
    # カーソルオブジェクトの作成

    sql = 'INSERT INTO Thread(name, details) VALUES("' + \
        name + '", "' + details + '")'
    # threadテーブルへスレッド名と詳細の登録
    cur.execute(sql)

    sql = 'SELECT id FROM Thread ORDER BY id DESC LIMIT 1'
    # スレッドIDを抽出
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

    conn = sqlite3.connect("test.db")
    # データベース作成
    cur = conn.cursor()
    # カーソルオブジェクトの作成

    sql = 'SELECT * FROM Thread WHERE id=' + str(id)
    # スレッドIDを抽出
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

    if (len(searchWords) != 0) or (len(searchTags) != 0):
        # searchWordsとsearchTagsの要素数が0でなければif文に入る
        sql += ' WHERE'
        if len(searchWords) != 0:
            # searchWordsの要素数が0でなければif文に入る
            for searchWord in searchWords:
                sql += (' name LIKE "%' + searchWord + '%" OR')
                # searchWordをsql文に追加
        if len(searchTags) != 0:
            # searchTagsの要素数が0でなければif文に入る
            for searchTag in searchTags:
                sql += (' tags LIKE "%' + searchTag + '%" OR')
                # searchTagをsql文に追加
        sql = sql.rstrip(' OR')
        # 右からORを探して見つけたら削除
    cur.execute(sql)
    results = cur.fetchall()

    for result in results:
        id = result[0]
        new = classes.Thread.getThread(id)
        resultThreads.append(new)
        # resultThreadにnewThreadを追加

    cur.close()
    conn.close()

    return resultThreads
