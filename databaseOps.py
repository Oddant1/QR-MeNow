import sqlite3 as sql
def intialDatabaseCreation():
   conn = sql.connect('database.db')
   print("Opened database successfully");
   conn.execute('CREATE TABLE contacts (name TEXT, addr TEXT, city TEXT, email TEXT)')
   conn.execute('CREATE TABLE qrCodes (account TEXT, query TEXT, uses integer )')
   print("Table created successfully");
   conn.close()

def queryDatabaseBySqlString( sqlString ):

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

def addDatabaseEntry(name, address, city, email):
   try:
      with sql.connect("database.db") as con:
         cur = con.cursor()
         cur.execute("INSERT INTO contacts (name,addr,city,email) VALUES (?,?,?,?)", (name, address, city, email))
         con.commit()
         con.close()
         returnMessage ="Record successfully added"
   except:
      con.rollback()

      returnMessage = "Error in insert operation"

   finally:
      con.close()
      return returnMessage

