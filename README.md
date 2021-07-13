# ShibauraBBS

## Overview
WebSocketを用いた掲示板
※芝浦学生のみ

## How to work
### パッケージ
- Flask
- Flask-SocketIO
- PyJWT
- cryptography
- gevent

### インストール
```
pip install flask flask-socketio pyjwt cryptography gevent
```

###  実行
#### DBの初期化
```
python createDB.py
```
#### サーバの場合
```
python server.py
```
#### ローカル環境の場合
```
python app.py
```

## グループ
5班
