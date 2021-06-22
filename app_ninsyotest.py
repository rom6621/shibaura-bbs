from logging import debug
from flask import Flask, render_template, redirect, url_for
from local_settings import cliend_id
from flask_socketio import SocketIO, emit

import dealAuth
from pprint import pprint

app = Flask(__name__)
socketio = SocketIO(app)

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
    return render_template('thread.html')

@app.route('/threadList')
def displayThreadList():
    return render_template('threadList.html')

@app.route('/test')
def test():
    return redirect(url_for('displayThreadList'))

@socketio.on('checkToken')
def checkToken(token) :
    userID=dealAuth.takingGoogleMailProcessing(token)
    print(userID)
    if (userID == None) :
        print('a')
    else :
        print('b')


# 実行
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0' ,port=5000)
