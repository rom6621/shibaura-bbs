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

###  実行方法
#### DBの初期化
```
python createDB.py
```
#### 50500ポートで実行する場合
```
python server.py
```
#### 5000ポートで実行する場合
```
python app.py
```

## グループ
5班
