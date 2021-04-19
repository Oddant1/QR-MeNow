import hostServer
import accountBackEnd
import databaseOps


def run():
    # Script for simulating user interaction
    try:
        databaseOps.intialDatabaseCreation()
    except:
        pass
    username = "Kate33"
    password = "HelloWorldThisIsAPassword"
    FirstName = "Kate"
    LastName = "Newman"
    PhoneNumber = "928353461"
    Address = "1789 S Failing Finals ST Flagstaff AZ 86001"
    Email = "GivingMENothing@gmail.com"
    qrStirng = f"Name: {FirstName} {LastName} \nPhoneNumber: {PhoneNumber}\nAddress: {Address}\nEmail: {Email}"
    userID = databaseOps.getUserID(username)
    accountBackEnd.add_account_to_data_base(username, password)
    databaseOps.addDatabaseEntry(userID, FirstName, LastName, PhoneNumber, Address, Email)
    databaseOps.addQrDataEntry(userID, username, qrStirng)

if __name__ == '__main__':
    run()