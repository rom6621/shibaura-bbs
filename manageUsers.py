#################################################
### Designer : 鈴木 一史
### Date : 2021.06.11
### Purpose : DBに利用者情報を問い合わせ、登録済みであればUserIDとMailAddressを返し、
###            なければ、登録してUseIDとMailAddressを返す。
#################################################

#################################################
### Function Name : userRegistrationRequest
### Designer : 鈴木一史
### Date : 2021.06.11
### Function: DBに利用者情報を問い合わせ、登録済みであればUserIDとMailAddressを返し、
###            なければ、登録してUseIDとMailAddressを返す。
### Return : Userクラス
#################################################
import sqlite3
import classes

def userRegistrationRequest(mailAddress):
    dbname = 'test.db' #データベース作成　or 参照
    conn = sqlite3.connect(dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    id = ''
    #DBの中のtableの中身を確認
    cur.execute('SELECT mailAddress FROM User WHERE mailAddress = "%s"' % mailAddress)
    row = cur.fetchall()

    #DB内になかった場合ユーザIDに作成したidを代入し、ユーザidとメールアドレスをもったクラスを返す
    if len(row) == 0 :
        #ユーザID作成処理
        id = mailAddress.split("@")[0]

        #tableへの登録
        sql = 'INSERT INTO User(id, mailAddress,name) values ("' + id + '", "' + mailAddress + '","noName )'
        cur.execute(sql)


    #DB内にあったとき
    else:
        #行を再取得
        cur.execute('SELECT id,name FROM User WHERE mailAddress = "%s"' % mailAddress)
        row = cur.fetchone()


        #tableがまだ決まっていないのでrow[0](UseID)
        id = row[0]
        name = row[1]

    tmpUser = classes.User(id, mailAddress,name)
    cur.close()
    conn.commit()
    conn.close()
    return tmpUser

#################################################
### Function Name : userNameUpdate
### Designer : 鈴木一史
### Date : 2021.06.11
### Function: DBに利用者情報を問い合わせ、ユーザ名の更新を行う。
### Return : User   クラス
#################################################

def userNameUpdate(uclass,nName):
    id = uclass.id

    dbname = 'test.db' #データベース作成　or 参照
    conn = sqlite3.connect(dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    cur.execute('UPDATE User SET name = "' + nName + '" WHERE id = "' + id + '"')
    uclass.name = nName

    cur.close()
    conn.commit()
    conn.close()
    return uclass