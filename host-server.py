from QRCode import QRCode

from flask import Flask, render_template, request
import sqlite3 as sql
import flask_qrcode
app = Flask(__name__)
qrcode = flask_qrcode.QRcode(app)

# global var
homepageTemplate = "home.html"
newDatabaseEntryTemplate = "contact.html"
showResultTemplate = "result.html"
newQRCodeTemplate = "new-qr-code.html"
showQRCodeTemplate = "show-qr-code.html"
QRCodes = []

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/enternew')
def new_contact():
   return render_template("contact.html")

@app.route('/genQRCode')
def new_qrCode():
   return render_template("genQRCode.html")

@app.route('/newCode', methods = ['POST', 'GET'])
def new_student():
   if request.method == 'POST':
      name = request.form['name']
      address = request.form['address']
      city = request.form['city']
      email = request.form['email']

      fullString = "Name: " + name + "\n"
      fullString += "address: " + address + "\n"
      fullString += "city: " + city + "\n"
      fullString += "email: " + email + "\n"

      QRCodes.append(QRCode(fullString))
      return render_template("newCode.html", qrString=fullString)

@app.route('/storedQRCodes')
def stored_codes():
   return render_template("storedQRCodes.html", qrcodes=QRCodes)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         address = request.form['address']
         city = request.form['city']
         email = request.form['email']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO contacts (name,addr,city,email) VALUES (?,?,?,?)",(name,address,city,email) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "Error in insert operation"

      finally:
         con.close()
         return render_template("result.html",msg = msg)


@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from contacts")

   rows = cur.fetchall();

   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
