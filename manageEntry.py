#################################################
### Designer : 
### Date : 
### Purpose : 
#################################################

#################################################
### Function Name : 
### Designer : 
### Date : 
### Function: 
### Return : 
#################################################
import sqlite3

#書込情報問い合わせ
#user_idとcontents_idが一致する書込がデータベースにあると0を返し、なかったら1を返す
def Contents_Processing(userID,contentsID):
    conn = sqlite3.connect('DBS.db')
    c = conn.cursor()
    if(c.execute('SELECT CONTENTS FROM BBSManage WHERE USER_ID = "'+userID +'" AND CONTENTS_ID = '+str(contentsID))!=None):
        #書込があったとき
        conn.close()
        return 0
    else:
        #書込がなかったとき
        conn.close()
        return 1


#書込削除
#user_idとcontents_idが一致する書込を更新する
def Delete_Contents(userID,contentsID):
    conn = sqlite3.connect('DBS.db')
    c = conn.cursor()
    data=('書込を削除しました.')
    c.execute('UPDATE BBSManage SET CONTENTS = "'+data+'" WHERE USER_ID = "'+userID+'" AND CONTENTS_ID = '+str(contentsID))
    conn.close()


#書込追加
#書込を追加する
def Add_Contents(userID,contentsID,contents):
    conn = sqlite3.connect('DBS.db')
    c = conn.cursor()
    c.execute('INSERT INTO BBSManage VALUES("'+userID+'", ' +str(contentsID)+', "' +contents+ '")')
    conn.close()
