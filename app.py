from threading import Thread
from flask import Flask, render_template, redirect, url_for, request
from local_settings import cliend_id
from flask_socketio import SocketIO, emit
import thread

app = Flask(__name__)
socketio = SocketIO(app)

###################テストデータ###################

test1 = thread.Thread(1, "テストスレッド1", "1つ目のスレッド")
test2 = thread.Thread(2, "テストスレッド2", "2つ目のスレッド")
test3 = thread.Thread(3, "テストスレッド2", "2つ目のスレッド")

for i in range(5):
    test1.addEntry('名無し', str(i) + "個目の書込です")
    test2.addEntry('名無し', str(i) + "個目の書込です")
    test3.addEntry('名無し', str(i) + "個目の書込です")

threads = [test1, test2, test3]

#################################################

@app.route('/')
def index():
    return render_template('threadList.html')

@app.route('/login')
def login():
    return render_template('login.html', cliend_id=cliend_id)

@app.route('/makeThread')
def makeThread():
    return render_template('makeThread.html')

@app.route('/thread')
def displayThread():
    return render_template('thread.html', thread = test1)

@app.route('/threadList')
def displayThreadList():
    return render_template('threadList.html', threads=threads)

@socketio.on('checkToken')
def checkToken(token):
    print(token)
    return render_template('threadList.html')

# 実行
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
