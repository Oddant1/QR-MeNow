from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlite3
import sqlite3 as sql
1
app = Flask(__name__)

logInPage = 'logIn.html'
signUpPage = 'signUp.html'


@app.route('/')
def home():
    return render_template('testerLandingPageForAccountLogin.html')


@app.route('/signUp', methods=['POST', 'GET'])
def sign_up():
    print(request)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        add_account_to_data_base(username, password)
        return render_template("signUp.html")
    return render_template("signUp.html", method='POST')


@app.route('/logIn', methods=['POST', 'GET'])
def log_in():
    if request.method == 'POST':
        try:
            given_username = request.form['username']
            given_password = request.form['password']
            with sql.connect("accounts.db") as con:
                cur = con.cursor()
                results = cur.execute("SELECT username, password "
                                      "FROM users WHERE username = ?", (given_username,))

                results = cur.fetchone()
                if results is not None:
                    db_user, db_password = results
                    print(results)
                    if given_username == db_user and given_password == db_password:
                        print('you are now logged in boiiii')
                    else:
                        print('sucks to suck dont it')

        except Exception as e:
            print(e)
    return render_template("logIn.html", method='POST')


def add_account_to_data_base(username, password):
    try:
        with sql.connect("accounts.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (username,password) VALUES (?,?)",
                        (username, password))
            con.commit()
            print('account made')
    except Exception as e:
        print(e)


# this shit doesnt work need to find fix
def intialDatabaseCreation():
    conn = sql.connect('accounts.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE users (username TEXT, password TEXT)')
    print("table created successfully")
    conn.close()


if __name__ == '__main__':
    # Create database if not already created
    try:
        intialDatabaseCreation()
    except:
        print("Database Already Created")

    app.run(debug=True, host='127.0.0.1', port=5000)
