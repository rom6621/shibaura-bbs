#################################################
### Designer : 保科貴大
### Date : 2021.6.18
### Purpose : 書込情報管理部
#################################################

import sqlite3
import clasees


#################################################
### Function Name : contentsProcessing
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDからcontentを抜き出しcontentが
###　　　　　　があるなら0,ないなら1を返す
### Return : 0または1
#################################################

#書込情報問い合わせ
#user_idとcontents_idが一致する書込がデータベースにあると0を返し、なかったら1を返す
def contentsProcessing(threadId):
    entries = []
     #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #Entryテーブルからcontentを抜き出す
    c.execute('SELECT * FROM Entry WHERE threadId = '+str(threadId)+' ORDER BY id ASC  ')
    results = c.fetchall()
    for(result in results):
        id = result[0]
        auther = result[2]
        content = result[3]
        new = clasees.Entry(id,auther,content)
        entries.append(new)
    conn.close()
    return entries
    


#################################################
### Function Name : deleteContents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDからcontentを指定して
###　　　　　　"書込を削除しました"に変更する
### Return : 
#################################################

#書込削除
#user_idとcontents_idが一致する書込を更新する
def deleteContents(userID,contentID):
     #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    data=('書込を削除しました.')
    #contentを更新する
    c.execute('UPDATE Entry SET content = "'+data+'" WHERE auther = "'+userID+'" AND id = '+str(contentID)+'')
    conn.commit()
    conn.close()



#################################################
### Function Name : addContents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDとcontentをDBに登録する
### Return : 
#################################################

#書込追加
#書込を追加する
def addContents(userID,threadID,content):
    #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #userID,threadID,contentをEntryテーブルに追加する
    c.execute('INSERT INTO Entry(auther,threadID,content) VALUES("'+userID+'",'+str(threadID)+',"'+content+'")')
    conn.commit()
    conn.close()
