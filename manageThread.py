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
import classes
# スレッド情報登録


def threadRegistration(name, details):

    conn = sqlite3.connect("test.db")
    # データベース作成
    cur = conn.cursor()
    # カーソルオブジェクトの作成

    sql = 'INSERT INTO Thread (name, details) values ("' + \
        name + '","' + details + '")'
    # threadテーブルへスレッド名と詳細の登録
    cur.execute(sql)

    sql = 'SELECT threadID FROM Thread ORDER BY threadID DESC LIMIT 1'
    # スレッドIDを抽出
    cur.execute(sql)

    threadId = cur.fetchall[0]

    cur.close()
    conn.close()

    newThread = clasees.Thread(threadId, name, details)
    # newThreadにスレッドの情報を入れる
    return newThread


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

    sql = 'SELECT * FROM Thread'

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
                sql += ('tags LIKE "%' + searchTag + '%" OR')
                # searchTagをsql文に追加
        sql = sql.rstrip(' OR')
        # 右からORを探して見つけたら削除
    cur.execute(sql)
    results = cur.fetchall()

    for result in results:
        id = result[0]
        name = result[1]
        details = result[2]
        newThread = clasees.Thread(id, name, details)
        resultThreads.append(newThread)
        # resultThreadにnewThreadを追加

    cur.close()
    conn.close()

    return resultThreads
