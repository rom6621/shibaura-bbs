import re
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True

socketio = SocketIO(app)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/makeThread')
def makeThread():
    return render_template('makeThread.html')

@app.route('/thread')
def displayThread():
    return render_template('thread.html')

@app.route('/threadList')
def displayThreadList():
    return render_template('threadList.html')

# 実行
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0' ,port=5000)
