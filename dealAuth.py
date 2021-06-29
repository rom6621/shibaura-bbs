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
###          メールアドレスを導き出し，芝浦のものの場合，利用者
###          情報管理部に問い合わせ&登録を行う．
### Return :user_id     --ユーザID
#################################################

def takingGoogleMailProcessing(token):
    jwksURI = 'https://www.googleapis.com/oauth2/v3/certs'
    googleIssuer = 'accounts.google.com'
    clientID = cliend_id

    #受け取ったtokenからid_tokenを探すfor文
    for keyFirst in token :
        for keySecond in token[keyFirst] :
            if (keySecond == 'id_token') :
                idToken = token[keyFirst][keySecond] #tokenの中にあるid_tokenの中身

    header = jwt.get_unverified_header(idToken) #id_tokenの中にあるheader
    res = requests.get(jwksURI).json() #JWKS_URI内にあるjsonファイルの中身
    jwk = next(filter(lambda k: k['kid'] == header['kid'], res['keys'])) #res内にあるデコードに必要な情報
    public_key = RSAAlgorithm.from_jwk(json.dumps(jwk)) #jwkを元にしたデコード用の鍵

    claims = jwt.decode(idToken,
                        public_key,
                        issuer=googleIssuer,
                        algorithms=['RS256'],
                        audience=clientID) #id_tokenのデコード用

    gmailAddress = claims['email'] #Googleのメアド
    invaderCheck = gmailAddress.split('@') #外部のGoogleアカウントのチェック用

    #芝浦のGoogleアカウントかどうかの確認、芝浦のものならば問い合わせ&登録を行う
    if (invaderCheck[1] == 'shibaura-it.ac.jp') :
        return userRegistrationRequest(mailAddress)
    else :
        return None
