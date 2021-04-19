import databaseOps

# mock object of empty database for testing
try:
    databaseOps.intialDatabaseCreation()
except:
    print("Database Already Created")


def test_addQrDataEntry():
    assert databaseOps.addQrDataEntry(123, "testusername", "qrteststring") == "Record successfully added"

def test_addDatabaseEntry():
    assert databaseOps.addDatabaseEntry(123, "Fname", "Lname", 123-456-7891, "123 W Test St", "test@test.com") == "Record successfully added"

def test_queryDatabaseBySqlString():
    assert databaseOps.queryDatabaseBySqlString("SELECT username FROM qrcodes") == [('testusername',)]

def test_getQrCode():
    assert databaseOps.getQrCode(123) == ('qrteststring',)

def test_deleteQrCodeFromDB():
    assert databaseOps.deleteQrCodeFromDB(123) == None
