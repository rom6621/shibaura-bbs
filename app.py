from flask import Flask, render_template
from local_settings import cliend_id

app = Flask(__name__)
app.debug = True

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

# 実行
if __name__ == '__main__':
    app.run()
