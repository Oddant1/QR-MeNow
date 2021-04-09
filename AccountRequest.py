import sqlite3 as sql

import flask_login

from flask import Flask
from flask_login import LoginManager, current_user
# from flask_login import UserMixin
# from flask_login import login_required
# from flask_login import login_user
# from flask_login import logout_user
from User import *
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
import bcrypt


# create app
app = Flask(__name__)
# login_manager = LoginManager(app)


app.secret_key = 'xxxxyyyyyzzzzz'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/signUp', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        add_account_to_data_base(username, password)
        return render_template("signUp.html")
    return render_template("signUp.html", method='POST')




@app.route('/logIn', methods=['POST', 'GET'])
def log_in():
    # if current_user.is_authenticated:
    #     return render_template('home.html')

    if request.method == 'POST':
        # try:
        given_username = request.form['username']
        given_password = request.form['password']
        with sql.connect("accounts.db") as con:
            cur = con.cursor()
            results = cur.execute("SELECT id, username, password "
                                  "FROM users WHERE username = ?", (given_username,))
            results = cur.fetchone()
            print(results)
            if results is not None:
                accountId, db_user, db_password = results
                if given_username == db_user and bcrypt.checkpw(given_password.encode('utf8'), db_password):

                    user = cur.fetchone()
                    print(user)
                    loadedUser = User(accountId,"fake",db_password)
                    print(type(loadedUser))
                    login_user(loadedUser, remember=False, duration=None, force=False, fresh=True)
                    flash('Logged in successfully ')

                    return render_template('testerLandingPageForAccountLogin.html')
                else:
                    flash('Login Unsuccessfull.')
        #
        # except Exception as e:
        #    print(e)

    return render_template("logIn.html", method='POST')


#     if request.method == 'POST':
#       #  try:
#         given_username = request.form['username']
#         given_password = request.form['password']
#         with sql.connect("accounts.db") as con:
#             cur = con.cursor()
#             results = cur.execute("SELECT id, username, password "
#                                   "FROM users WHERE username = ?", (given_username,))
#             results = cur.fetchone()
#             if results is not None:
#                 accountId, db_user, db_password = results
#                 if given_username == db_user and bcrypt.checkpw(given_password.encode('utf8'), db_password):
#
#                     print(accountId)
#
#                     flash("Logged in successfully")
#                     return redirect('home')
#                 else:
#                     print('sucks to suck dont it')
#
#         # except Exception as e:
#         #     print(e)
#     return render_template("logIn.html", method='POST')

def add_account_to_data_base(username, password):
    try:
        with sql.connect("accounts.db") as con:
            cur = con.cursor()
            hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)",
                        (username, hashed))
            con.commit()
            accountId = cur.execute("SELECT id "
                                    "FROM users WHERE username = ?", (username,)).fetchone()[0]
            print(accountId)
            print('account made')
    except Exception as e:
        print(e)


def intialDatabaseCreation():
    conn = sql.connect('accounts.db')
    print("Opened database successfully");
    conn.execute('CREATE TABLE users (id integer primary key autoincrement , username TEXT , password TEXT )')
    conn.execute('CREATE TABLE contacts (name TEXT, addr TEXT, city TEXT, email TEXT)')
    conn.execute('CREATE TABLE qrCodes (account TEXT, query TEXT, uses integer )')
    print("Table created successfully");
    conn.close()


try:
    print('try')
    intialDatabaseCreation()
except Exception as e:
    print(e)
    print("Database Already Created")
app.run(debug=True, host='127.0.0.1', port=8080)
