from datetime import timedelta
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3 as sql
import flask_qrcode
import bcrypt
import databaseOps
import accountBackEnd

# app set up
app = Flask(__name__)
qrcode = flask_qrcode.QRcode(app)
app.secret_key = "912047fgdsbv8d90bvs7890vufds"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    print(session)
    return render_template("home.html")


@app.route('/signUp', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # adding account to db
        accountBackEnd.add_account_to_data_base(username, password)
        return render_template("home.html")
    return render_template("signUp.html", method='POST')


@app.route('/logIn', methods=['POST', 'GET'])
def log_in():
    print(request.method)
    if request.method == 'POST':
        given_username = request.form['username']
        given_password = request.form['password']
        with sql.connect("database.db") as con:
            cur = con.cursor()
            results = cur.execute("SELECT userid, username, password "
                                  "FROM users WHERE username = ?", (given_username,))
            results = cur.fetchone()
            if results is not None:
                accountId, db_user, db_password = results
                if given_username == db_user and bcrypt.checkpw(given_password.encode('utf8'), db_password):
                    session["user"] = given_username
                    session.permanent = True
                    return redirect(url_for('home'))
                else:
                    print('sucks to suck dont it')
                    return redirect(url_for("log_in"))

    return render_template("logIn.html", method='POST')


@app.route('/enternew')
def newContact():
    if "user" in session:
        # returns the page for entering a new contact
        return render_template("contact.html")
    else:
        return redirect(url_for('log_in'))


@app.route('/genQRCode')
def newQRCode():
    if "user" in session:
        # returns the page for generating a new qr code
        user = session["user"]
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select fname, lname, phonenumber, addr, email from contacts WHERE userid = ?",
                    (getUserId(user),))
        rows = cur.fetchone()
        return render_template("genQRCode.html", rows=rows)
    else:
        return redirect(url_for('log_in'))


@app.route('/sqlTest')
def newSQLQuery():
    # give a page where you can enter a sql query(yay for injection)
    return render_template("sqlTest.html")


@app.route('/newCode', methods=['POST', 'GET'])
def newCode():
    if "user" in session:
        if request.method == 'POST':
            user = session["user"]
            con = sql.connect("database.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("select fname, lname, phonenumber, addr, email from contacts WHERE userid = ?",
                        (getUserId(user),))
            userCodeData = cur.fetchone()
            # breaking up the sql response to get user data
            firstName = userCodeData[0]
            lastName = userCodeData[1]
            phoneNumber = userCodeData[2]
            address = userCodeData[3]
            email = userCodeData[4]
            name = "" + firstName + " " + lastName
            # append the gleaned information to a string
            fullString = "Name: " + name + "\n"
            fullString += "Phone Number: " + phoneNumber + "\n"
            fullString += "Address: " + address + "\n"
            fullString += "Email: " + email + "\n"
            # adding qr sting to the db back end
            databaseOps.addQrDataEntry(getUserId(user), user, fullString)
            return render_template("newCode.html", qrString=fullString)
        else:
            return redirect(url_for("newQRCode", _method="POST"))
    else:
        return redirect(url_for('log_in'))


@app.route('/QueryResult', methods=['POST', 'GET'])
def queryDatabase():
    if request.method == 'POST':
        # read in the sql query from the post request
        sqlQuery = str(request.form['sql'])
        sqlResult = databaseOps.queryDatabaseBySqlString(sqlQuery)
        return render_template("newCode.html", qrString=sqlResult)


@app.route('/storedQRCodes')
def storedCodes():
    if "user" in session:
        user = session["user"]
        QRCode = databaseOps.getQrCode(getUserId(user))
        if QRCode == None:
            return render_template("storedQRCodes.html")
        return render_template("storedQRCodes.html", qrcodes=QRCode)


@app.route('/deleteQRCode', methods=['POST'])
def deleteCode():
    user = session["user"]
    userId = getUserId(user)
    databaseOps.deleteQrCodeFromDB(userId)
    return render_template("storedQRCodes.html")


@app.route('/addRecord', methods=['POST', 'GET'])
def addRecord():
    if "user" in session:
        user = session["user"]
        if request.method == 'POST':
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            phoneNumber = request.form['phone']
            address = request.form['address']
            email = request.form['email']
            userid = getUserId(user)
            # call to back end db manager to add data
            databaseReponseMessage = databaseOps.addDatabaseEntry(userid, firstName, lastName, address, phoneNumber,
                                                                  email)
            print(databaseReponseMessage)
            return redirect(url_for('home'))
    else:
        return redirect(url_for('log_in'))


@app.route('/contactInfoList')
def listContactInfo():
    if "user" in session:
        user = session["user"]
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select fname, lname, phonenumber, addr, email from contacts WHERE userid = ?", (getUserId(user),))
        rows = cur.fetchone()
        print(rows['fname'])
        return render_template("listAllEntries.html", rows=rows)
    else:
        return redirect(url_for('log_in'))


@app.route('/logout')
def logout():
    print(f"Logging out user from session{session}")
    session.pop("user", None)
    print(f"Session is now {session}")
    return redirect(url_for("home"))


def getUserId(username):
    if "user" in session:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            userId = cur.execute("SELECT userid "
                                 "FROM users WHERE username = ?", (username,)).fetchone()[0]
            return userId
    else:
        return redirect(url_for("log_in"))



if __name__ == '__main__':
    # Create database if not already created
    try:
        databaseOps.intialDatabaseCreation()
    except:
        print("Database Already Created")

    app.run(debug=True, host='0.0.0.0', port=8080)
