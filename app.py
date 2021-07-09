#################################################
### Designer : 浅瀬石 遊那, 佐藤直輝
### Date :2021.07.09
### Purpose : C1のUIの入出力を処理する
#################################################

### Revision :
### V1.0 : 開米, 2021.06.13
### V1.1 : 開米, 2021.06.15 writeEntry, deleteEntry
### V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く
### V1.3 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く

from os import name
from manageUsers import userNameUpdate
from flask import Flask, render_template, redirect, url_for, request, session
from local_settings import cliend_id, secret_key
from flask_socketio import SocketIO
import json
import classes, thread, dealAuth

app = Flask(__name__)
app.secret_key = secret_key
socketio = SocketIO(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

#################################################
### Function Name : ログイン・マイページ処理
### Designer : 浅瀬石 遊那
### Date :2021.06.13
### Function: ログイン画面やマイページ処理からの入出力を処理する
### Return : ログイン画面，マイページ画面
#################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        token = json.loads(request.form['token'])
        user = dealAuth.takingGoogleMailProcessing(token)
        if user != None:
            session['userId'] = user.id
            session['userName'] = user.name
            return redirect(url_for('displayThreadList'))
        else:
            return render_template('login.html', cliend_id=cliend_id, login=False)
    else:
        if 'userId' in session:
            session.clear()
            return redirect(url_for('displayThreadList'))
        else:
            return render_template('login.html', cliend_id=cliend_id)

@app.route('/mypage', methods=['GET', 'POST'])
def displayMypage():
    if 'userId' in session:
        if request.method == 'POST':
            userName = request.form['userName']
            classes.updateName(session['userId'], userName)
            session['userName'] = userName
            return render_template('mypage.html')
        else:
            return render_template('mypage.html')
    else:
        return redirect(url_for('login'))

#################################################
### Function Name : スレッド処理
### Designer : 佐藤 直輝
### Date :2021.07.9
### Function: スレッド作成やスレッド一覧画面を出力する
### Return : スレッド作成画面, スレッド一覧画面
#################################################

@app.route('/makeThread', methods=['GET', 'POST'])
def makeThread():
    if 'userId' in session:
        if request.method == 'POST':
            name = request.form['name']
            details = request.form['details']
            thread = classes.Thread.createThread(name, details)
            return redirect(url_for('displayThread', thread=thread.id))
        else:
            return render_template('makeThread.html')
    else:
        return redirect(url_for('login'))

@app.route('/threadList', methods=['GET'])
def displayThreadList():
    if 'userId' in session:
        if request.args.get('search'):
            search = request.args.get('search')
            threads = thread.analyzeKeyword(search)
        else:
            search = ""
        threads = thread.analyzeKeyword(search)
        return render_template('threadList.html', threads=threads)
    else:
        return redirect(url_for('login'))

#################################################
### Function Name : スレッド表示処理
### Designer : 佐藤 直輝
### Date :2021.07.6
### Function: スレッド画面を表示する
### Return : スレッド画面
#################################################

@app.route('/thread', methods=['GET'])
def displayThread():
    if 'userId' in session:
        id = request.args.get('thread')
        thread = classes.Thread.getThread(id)
        return render_template('thread.html', thread=thread)
    else:
        return redirect(url_for('login'))

@socketio.on('write board')
def writeBoard(args):
    threadId = args['threadId']
    content = args['content']
    entry = classes.Thread.getThread(threadId).addEntry(classes.User.getUser(session['userId']), content)
    param = {'threadId': threadId, 'entryId': entry.id, 'entryAuthor': entry.author.name, 'authorId': entry.author.id, 'entryContent': entry.content}
    socketio.emit('add entry', param)

@socketio.on('delete entry')
def deleteEntry(args):
    threadId = args['threadId']
    entryId = args['entryId']
    classes.Thread.getThread(threadId).deleteEntry(int(entryId))
    param = {'threadId': threadId, 'entryId': entryId}
    socketio.emit('update entry', param)

# 実行
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
