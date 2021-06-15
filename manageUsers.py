#################################################
### Designer : 鈴木 一史
### Date : 2021.06.11
### Purpose : DBに利用者情報を問い合わせ、登録済みであればUserIDとMailAddressを返し、
###            なければ、登録してUseIDとMailAddressを返す。
#################################################

#################################################
### Function Name : User_Registration_Request
### Designer : 鈴木一史
### Date : 2021.06.11
### Function: DBに利用者情報を問い合わせ、登録済みであればUserIDとMailAddressを返し、
###            なければ、登録してUseIDとMailAddressを返す。
### Return : UserID,MailAddress
#################################################
import sqlite3
import user

def User_Registration_Request(mailAddress):
    dbname = 'BBS.db' #データベース作成　or 参照
    conn = sqlite3.connect(dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    id = ''
    #DBの中のtableの中身を確認
    cur.execute('SELECT mailAddress FROM User WHERE mailAddress = ' + mailAddress)
    
    #DB内になかった場合ユーザIDにNullを代入し、メールアドレスを返す
    if cur.fetchall() ==None :
        #ユーザID作成処理
        id = mailAddress.split("@")[0]

        #tableへの登録
        sql = 'INSERT INTO User (userId, mailAddress) values (' + id + ',' + mailAddress + ')'
        cur.execute(sql)


    #DB内にあったとき
    else:
        row = cur.fetchall()
        #tableがまだ決まっていないのでrow[0](UseID)
        id = row[0]

    tmpUser = user.User(id, mailAddress)

    conn.close()
    return user