from databaseOps import *
from accountBackEnd import *
import pytest

def test_account():

    try:
        intialDatabaseCreation()
    except:
        print("Database already created")

    username = "hello"
    password = "world"

    add_account_to_data_base(username, password)

    userID = int(getUserID(username))

    first_name = "John"
    last_name = "Doe"
    phone_number = "123-456-7890"
    address = "1234 Address"
    email = "email@email.com"

    addDatabaseEntry(userID, first_name, last_name, address, phone_number, email)

    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT fname, lname, phonenumber, addr, email FROM contacts WHERE userid = ?", (userID,))
    rows = cur.fetchone()

    test_first_name = rows[0]
    test_last_name = rows[1]
    test_phone = rows[2]
    test_address = rows[3]
    test_email = rows[4]

    assert first_name == test_first_name
    assert last_name == test_last_name
    assert phone_number == test_phone
    assert address == test_address
    assert email == test_email

