#################################################
### File Name : dealAuth.py
### Version : V1.0
### Designer : 浅瀬石 遊那
### Date : 2021.06.11
### Purpose : 認証処理部
#################################################

import json
import jwt
from local_settings import cliend_id
from jwt.algorithms import RSAAlgorithm
from pprint import pprint
import requests
import manageUsers

#################################################
### Function Name :takingGoogleMailProcessing
### Designer :浅瀬石 遊那
### Date :2021.06.11
### Function:受け取ったtokenからそのtokenのgoogleアカウントの
###          メールアドレスを導き出す．
### Return :user_id     --ユーザID
#################################################

def takingGoogleMailProcessing(token):
    JWKS_URI = 'https://www.googleapis.com/oauth2/v3/certs'
    GOOGLE_ISSUER = 'accounts.google.com'
    CLIENT_ID = cliend_id
    id_token = token['qc']['id_token'] #tokenの中にあるid_tokenの中身
    header = jwt.get_unverified_header(id_token) #id_tokenの中にあるheader
    res = requests.get(JWKS_URI).json() #JWKS_URI内にあるjsonファイルの中身
    jwk = next(filter(lambda k: k['kid'] == header['kid'], res['keys'])) #res内にあるデコードに必要な情報
    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk)) #jwkを元にしたデコード用の鍵
    claims = jwt.decode(id_token,
                        public_key,
                        issuer=GOOGLE_ISSUER,
                        algorithms=['RS256'],
                        audience=CLIENT_ID) #id_tokenのデコード用
    #pprint(claims)
    gmail_address = claims['email'] #Googleのメアド
    invader_check = gmail_address.split('@') #外部のGoogleアカウントのチェック用
    user_id = None #ユーザID、外部の場合はNoneのまま返る
    #芝浦のGoogleアカウントかどうかの確認、芝浦のものならば問い合わせを行う
    if (invader_check[1] == 'shibaura-it.ac.jp') :
        user_id = questionGmailProcessing(gmail_address)
        #未登録かどうかの確認、未登録ならば登録を行う
        if (user_id == None) :
            user_id = makingAccountProcessing(gmail_address)
    return user_id

#################################################
### Function Name :questionGmailProcessing
### Designer :浅瀬石 遊那
### Date :2021.06.11
### Function:受け取った学内のGmailアドレスを用い、
###          利用者情報管理部に問い合わせを行う
### Return :user_id     --ユーザID
#################################################

def questionGmailProcessing(gmail_address):
    user_data = manageUsers.user_Registration_Request(gmail_address)
    user_id = user_data[0]
    gmail_address = user_data[1]
    return user_id

#################################################
### Function Name :makingAccountProcessing
### Designer :浅瀬石 遊那
### Date :2021.06.11
### Function:受け取った学内且つDBに未登録であるGmailアドレスを用い、
###          利用者情報管理部に登録要求を行う
### Return :user_id     --ユーザID
#################################################

def makingAccountProcessing(gmail):
    user_data = manageUsers.makingRequestFromUserProcessing(gmail)
    user_id = user_data[0]
    gmail_address = user_data[1]
    return user_id
