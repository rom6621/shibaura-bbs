#################################################
### Designer : 保科貴大
### Date : 2021.6.18
### Purpose : 書込情報管理部
#################################################

import sqlite3


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
def contentsProcessing(userID,contentID):
     #データベースに接続
    conn = sqlite3.connect('test.db')
    #sqliteを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    #Entryテーブルからcontentを抜き出す
    if(c.execute('SELECT content FROM Entry WHERE auther = "'+userID +'" AND id = '+str(contentID)+'')!=None):
        #書込があったとき
        conn.close()
        return 0
    else:
        #書込がなかったとき
        conn.close()
        return 1



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
