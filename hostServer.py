from qrCode import QRCode

from flask import Flask, render_template, request
import sqlite3 as sql
import flask_qrcode
import userProfile
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
def newContact():
   # returns the page for entering a new contact
   return render_template("contact.html")

@app.route('/genQRCode')
def newQRCode():
   # returns the page for generating a new qr code
   return render_template("genQRCode.html")

@app.route('/sqlTest')
def newSQLQuery():
   # give a page where you can enter a sql query(yay for injection)
   return render_template("sqlTest.html")

@app.route('/newCode', methods = ['POST', 'GET'])
def newStudent():
   if request.method == 'POST':
      # read in the post request with all of its information
      name = request.form['name']
      address = request.form['address']
      city = request.form['city']
      email = request.form['email']

      # append the gleaned information to a string
      fullString = "Name: " + name + "\n"
      fullString += "Address: " + address + "\n"
      fullString += "City: " + city + "\n"
      fullString += "Email: " + email + "\n"

      # render a qr code based on this thing
      QRCodes.append(QRCode(fullString))
      return render_template("newCode.html", qrString=fullString)


@app.route('/QueryResult', methods = ['POST', 'GET'])
def queryDatabase():
   if request.method == 'POST':
      # read in the sql query from the post request
      sqlQuery = str(request.form['sql'])
      with sql.connect("database.db") as con:
         cur = con.cursor()
         print("Query: " + sqlQuery)
         cur.execute(sqlQuery)
         queryResult = cur.fetchall()
         print("Result: "+ str(queryResult))
      return render_template("newCode.html", qrString=queryResult)

@app.route('/storedQRCodes')
def stored_codes():
   return render_template("storedQRCodes.html", qrcodes=QRCodes)

@app.route('/deleteQRCode', methods = ['POST'])
def delete_code():
   # This is a bit fragile but eh it works for now

   args = list(request.form.keys())
   index = int(args[0]) - 1
   code = QRCodes[index]
   QRCodes.remove(code)
   return render_template("storedQRCodes.html", qrcodes=QRCodes)

@app.route('/addrec',methods = ['POST', 'GET'])
def add_record():
   if request.method == 'POST':
      try:
         # read in the post request
         name = request.form['name']
         address = request.form['address']
         city = request.form['city']
         email = request.form['email']

         with sql.connect("database.db") as con:
            # read i
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

@app.route('/contactInfoList')
def list_contact_info():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from contacts")

   rows = cur.fetchall();
   return render_template("listAllEntries.html",rows = rows)


def intial_database_creation():
   conn = sql.connect('database.db')
   print("Opened database successfully");
   conn.execute('CREATE TABLE contacts (name TEXT, addr TEXT, city TEXT, email TEXT)')
   conn.execute('CREATE TABLE qrCodes (account TEXT, query TEXT, uses integer )')
   print("Table created successfully");
   conn.close()

if __name__ == '__main__':
   # Create database if not already created
   try:
        intial_database_creation()
   except:
      print("Database Already Created")

   app.run(debug = True, host='0.0.0.0', port=8080)
