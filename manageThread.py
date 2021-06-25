#################################################
# Designer :
# Date :
# Purpose :
#################################################

#################################################
# Function Name :
# Designer :
# Date :
# Function:
# Return :
#################################################

import sqlite3
import clasees
# スレッド情報登録


def threadRegistration(name, details):

    conn = sqlite3.connect("test.db")
    # データベース作成
    cur = conn.cursor()
    # カーソルオブジェクトの作成

    sql = 'INSERT INTO Thread (name, details) values ("' + \
        name + '","' + details + '")'
    # threadテーブルへスレッド名とタグ名の登録
    cur.execute(sql)

    sql = 'SELECT threadID FROM Thread ORDER BY threadID DESC LIMIT 1'
    # スレッドIDを抽出
    cur.execute(sql)

    threadId = cur.fetchall[0]

    cur.close()
    conn.close()

    newThread = clasees.Thread(threadId, name, details)

    return newThread


#################################################
# Function Name :search
# Designer :
# Date :
# Function:
# Return :
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
        sql += ' WHERE'
        if len(searchWords) != 0:
            sql += ' name IN ('
            for searchWord in searchWords:
                sql += (' "' + searchWord + '",')
            sql = sql.rstrip(',')
            sql += ')'
            if len(searchTags) != 0:
                sql += ' OR'
        if len(searchTags) != 0:
            sql += ' tags IN ('
            for searchTag in searchTags:
                sql += (' "' + searchTag + '",')
            sql = sql.rstrip(',')
            sql += ')'

    cur.execute(sql)
    results = cur.fetchall()

    for result in results:
        id = result[0]
        name = result[1]
        details = result[2]
        newThread = clasees.Thread(id, name, details)
        resultThreads.append(newThread)

    cur.close()
    conn.close()

    return resultThreads
