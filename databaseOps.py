import sqlite3 as sql


# set up db for program
def intialDatabaseCreation():
    conn = sql.connect('database.db')
    print("Opened database successfully");
    # contact info
    conn.execute('CREATE TABLE contacts (userid integer primary key, fname TEXT, lname TEXT, phonenumber TEXT, '
                 'addr TEXT, email TEXT)')
    # qr codes
    conn.execute('CREATE TABLE qrCodes (userid integer primary key, username TEXT, qrString TEXT )')
    # user
    conn.execute('CREATE TABLE users (userid integer primary key autoincrement , username TEXT NOT NULL , password '
                 'TEXT NOT NULL )')
    print("Table's created successfully");
    conn.close()


def queryDatabaseBySqlString(sqlString):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            print("Query: " + sqlString)
            cur.execute(sqlString)
            queryResult = cur.fetchall()
            print("Result: " + str(queryResult))

        return queryResult

    except:
        return "INVALID SQL QUERY"


# stores user's info for creating a qr code
def addQrDataEntry(userId, username, qrString):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO qrCodes (userid, username, qrString) VALUES (?,?,?) ",
                        (userId, username, qrString))
            con.commit()
            con.close()
            returnMessage = "Record successfully added"
    except Exception as e:
        print(e)
        con.rollback()
        returnMessage = "Error in insert operation"
    finally:
        con.close()
        return returnMessage


# get a users qr code
def getQrCode(userId):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT qrString FROM qrCodes WHERE userid = ?", (userId,))
            code = cur.fetchone()
            return code
    except Exception as e:
        print(e)


# adds contact info and links to users account
def addDatabaseEntry(userId, firstName, lastName, phonenumber, address, email):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO contacts (userid, fname, lname, addr, phonenumber, email) VALUES (?,?,?,?,?,?) ",
                        (userId, firstName, lastName, phonenumber, address, email))
            con.commit()
            con.close()
            returnMessage = "Record successfully added"
    except Exception as e:
        print(e)
        con.rollback()

        returnMessage = "Error in insert operation"

    finally:
        con.close()
        return returnMessage
