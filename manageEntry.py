#################################################
### Designer : 保科貴大
### Date : 2021.6.18
### Purpose : 書込情報管理部
#################################################

import sqlite3

#################################################
### Function Name : Contents_Processing
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDからcontentを抜き出しcontentが
###　　　　　　があるなら0,ないなら1を返す
### Return : 0または1
#################################################

#書込情報問い合わせ
#user_idとcontents_idが一致する書込がデータベースにあると0を返し、なかったら1を返す
def Contents_Processing(userID,contentID):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    if(c.execute('SELECT content FROM Entry WHERE auther = "'+userID +'" AND id = '+str(contentID)+'')!=None):
        #書込があったとき
        conn.close()
        return 0
    else:
        #書込がなかったとき
        conn.close()
        return 1



#################################################
### Function Name : Delete_Contents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDからcontentを指定して
###　　　　　　"書込を削除しました"に変更する
### Return : 
#################################################

#書込削除
#user_idとcontents_idが一致する書込を更新する
def Delete_Contents(userID,contentID):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=('書込を削除しました.')
    c.execute('UPDATE Entry SET content = "'+data+'" WHERE auther = "'+userID+'" AND id = '+str(contentID)+'')
    conn.commit()
    conn.close()

#################################################
### Function Name : Add_Contents
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDとcontentをDBに登録する
### Return : 
#################################################
#書込追加
#書込を追加する
def Add_Contents(userID,threadID,content):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('INSERT INTO Entry(auther,threadID,content) VALUES("'+userID+'",'+str(threadID)+',"'+content+'")')
    conn.commit()
    conn.close()
