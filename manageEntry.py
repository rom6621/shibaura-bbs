#################################################
### Designer : 保科貴大
### Date : 2021.6.18
### Purpose : 書込情報管理部
#################################################

import sqlite3
import classes
import manageUsers

#################################################
### Function Name : contentsProcessing
### Designer : 保科貴大
### Date :  2021.6.18
### Function: threadIdからthreadの書き込みを全て抜き出す
###　　　　　　
### Return : entries
#################################################

#書込情報問い合わせ

def contentsProcessing(threadId):
    entries = []
     #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #Entryテーブルからcontentを抜き出す
    c.execute('SELECT id, auther, content FROM Entry WHERE threadId = ' +str(threadId)+ ' ORDER BY id ASC  ')
    results = c.fetchall()
    for result in results:
        id = result[0]
        auther = classes.User.getUser(result[1])
        content = result[2]
        new = classes.Entry(id,auther,content)
        entries.append(new)
    c.close()
    conn.close()
    return entries


#################################################
### Function Name : deleteContents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: entry.idとthreadIdからcontentを指定して
###　　　　　　"書込を更新する
### Return :
#################################################

#書込削除

def deleteContents(entry, threadId):
     #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #contentを更新する
    print('UPDATE Entry SET content="' + entry.content + '" WHERE threadId="' + str(threadId) + '" AND id=' + str(entry.id) + '"')
    c.execute('UPDATE Entry SET content="' + entry.content + '" WHERE threadId="' + str(threadId) + '" AND id="' + str(entry.id) + '"')
    c.close()
    conn.commit()
    conn.close()


#################################################
### Function Name : addContents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: entry.auther,entry.content,threadをDBに登録する
### Return :
#################################################

#書込追加

def addContents(entry,threadId):
    #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #userID,threadID,contentをEntryテーブルに追加する
    c.execute('INSERT INTO Entry(auther,threadID,content) VALUES("' + entry.author.id + '",' + str(threadId) + ',"' + entry.content + '")')
    c.close()
    conn.commit()
    conn.close()
