import re
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

import sqlite3

from local_settings import cliend_id

app = Flask(__name__)
app.debug = True

socketio = SocketIO(app)

@app.route('/login')
def login():
    if request.method == 'GET':
        return render_template('login.html', cliend_id=cliend_id)

@app.route('/make_thread')
def make_thread():
    return render_template('make_thread.html')

@app.route('/thread_list')
def thread_list():
    return render_template('thread_list.html')

@app.route('/thread')
def index():
    with open('logs/tmp.txt', 'r') as f:
        logs_list = f.read().split('\n')
    return render_template('thread.html', logs=logs_list, async_mode=socketio.async_mode)

@socketio.on('receive')
def add_message(message):
    if message:
        with open('logs/tmp.txt', 'a') as f:
            f.write("\n" + message)
        emit("reflect", message, broadcast=True)

@socketio.on('login_check')
def login_check(message):
    print("\n\n" + message + "\n\n")

@socketio.on('reset')
def reset_txt():
    with open('logs/tmp.txt', 'w') as f:
        f.write('')
    emit("reload", broadcast=True)

# 実行
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0' ,port=5000)
