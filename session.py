from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'pien'
app.permanent_session_lifetime = timedelta(days = 1)

@app.route("/session")
def session(userID) :
    session.permanent = True
    session["user"] = userID
    session.modified = True
