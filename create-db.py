import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE contacts (name TEXT, addr TEXT, city TEXT, email TEXT)')
<<<<<<< HEAD

conn.execute('CREATE TABLE qrCodes (account TEXT, query TEXT, uses integer )')

=======
>>>>>>> 8a156d95ac4cfc398090b693d794b9a3dda30982
print("Table created successfully");
conn.close()
