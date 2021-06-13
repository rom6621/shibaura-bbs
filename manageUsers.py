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

def User_Registration_Request(MailAddress):
    dbname = 'BBS.db' #データベース作成　or 参照
    conn = sqlite3.connect(dbname)
    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    UserID = ''
    #DBの中のtableの中身を確認
    cur.execute('SELECT MailAddress FROM User WHERE MailAddress = '+MailAddress)
    
    #DB内になかった場合ユーザIDにNullを代入し、メールアドレスを返す
    if cur.fetchall() ==None :
        #ユーザID作成処理
        UserID = MailAddress.split("@")[0]

        #tableへの登録
        sql = 'INSERT INTO User (UserID, MailAddress) values ('+UserID+','+MailAddress+')'
        cur.execute(sql)


    #DB内にあったとき
    else:
        row = cur.fetchall()
        #tableがまだ決まっていないのでrow[1](UseID),row[2](Address)
        UserID = row[1] 
        MailAddress = row[2]

    return UserID,MailAddress