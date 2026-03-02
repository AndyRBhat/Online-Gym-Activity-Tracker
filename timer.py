from flask import Flask, request, render_template
import sqlite3
import os
import json

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("timer.html")
try:
    connection = sqlite3.connect('database/timer.db', check_same_thread=False)
    sql = connection.cursor()
except Exception as e:
    connection = None
    print("Database connection failed:", e)

sql.execute('''
create table if not exists users(
   id integer primary key autoincrement,
   username Text,
   password Integer
)''')

sql.execute('''
create table if not exists tracking(
    id integer primary key autoincrement,
    user_id Integer,
    time Text,
    exercise Text
)
''')

connection.commit()

def create_json(cursor):
    headers = list(map(lambda x: x[0], cursor.description))
    results = []

    for row in cursor.fetchall():
        rowData = {}
        for i, col in enumerate(row):
            rowData[headers[i]] = col
        results.append(rowData)

    return json.dumps(results)

def signup(username, password):
    if connection is None:
        return "error: Could not connect to database"
    data = sql.execute('''select * from users where username = ?''', [username])
    rows = data.fetchall()
    if rows:
        return "error: User already exists"
    else:
        sql.execute('''insert into users (username, password) values (?, ?) ''', [username, password])
        connection.commit()
        return str(sql.lastrowid)
    
def signin(username, password):
    if connection is None:
        return "error: Could not connect to database"
    data = sql.execute('''select * from users where username = ? and password = ?''', [username, password])
    rows = data.fetchone()
    if rows:
        return str(rows[0])
    else:
        return "error: Incorrect username/password"
    
def add(user_id, time, exercise):
    sql.execute('''insert into tracking
    (user_id, time, exercise) values (?, ?, ?)''',
     [user_id, time, exercise])
    connection.commit()
    return "ok"
def show(user_id):
    rows=sql.execute('''select * from tracking
    where user_id=?''', [user_id])
    json=create_json(rows)
    return json

@app.route("/timer.py")
def main():
    mode = request.args.get("mode")

    if mode == 'signup':
        return signup(request.args.get("username"),
                      request.args.get("password"))

    elif mode == 'login':
        return signin(request.args.get("username"),
                      request.args.get("password"))

    elif mode == 'add':
        return add(request.args.get("user_id"),
                   request.args.get("time"),
                   request.args.get("exercise"))

    elif mode == 'show':
        return show(request.args.get("user_id"))

    return ""

if __name__ == "__main__":
    app.run(debug=True)
