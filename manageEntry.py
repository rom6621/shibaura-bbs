#################################################
### Designer : 保科貴大
### Date : 2021.6.18
### Purpose : 書込情報管理部
#################################################

#################################################
### Function Name : Contents_Processing
### Designer : 保科貴大
### Date :  2021.6.18
### Function: userIDとcontentIDからcontentを抜き出しcontentが
###　　　　　　があるなら0,ないなら1を返す
### Return : 0または1
#################################################
import sqlite3

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


#書込削除
#user_idとcontents_idが一致する書込を更新する
def Delete_Contents(userID,contentID):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    data=('書込を削除しました.')
    c.execute('UPDATE Entry SET content = "'+data+'" WHERE auther = "'+userID+'" AND id = '+str(contentID)+'')
    conn.close()


#書込追加
#書込を追加する
def Add_Contents(userID,contentID,content):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('INSERT INTO Entry(id,auther,content) VALUES('+str(contentID)+',  "'+userID+'", "'+content+'")')
    conn.close()
