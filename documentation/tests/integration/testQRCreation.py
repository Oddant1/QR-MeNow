from databaseOps import *
import sqlite3 as sql
import pytest

def test_QRgeneration():

    try:
        intialDatabaseCreation()
    except:
        print("Database already created") 

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT fname, lname, phonenumber, addr, email FROM contacts WHERE userid = ?", (getUserID("hello"),))
    rows = cur.fetchone()

    fname = rows[0]
    lname = rows[1]
    phonenum = rows[2]
    addr = rows[3]
    email = rows[4]

    name = "" + fname + " " + lname

    QRString = "Name: " + name + "\n"
    QRString += "Phone Number: " + phonenum + "\n"
    QRString += "Address: " + addr + "\n"
    QRString += "Email: " + email + "\n"

    addQrDataEntry(getUserID("hello"), "hello", QRString)

    cur.execute("SELECT qrString FROM qrCodes WHERE userid = ?", (getUserID("hello"),)) 
    QRrows = cur.fetchone()
    testQRString = QRrows[0]

    assert testQRString == QRString

