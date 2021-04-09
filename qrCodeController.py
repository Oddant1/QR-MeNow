from userProfileHandler import *
import time

class controller:

    firstName = getFirstName()
    lastName = getLastName()
    phone = getPhoneNumber()
    address = getAddress()
    email = getEmail()

    user = make_user_profile(firstName, lastName, phone, address, email)
    
    def pauseCode(user):
        user.deleteQR()

    def resumeCode(user):
        user.generateQR()

    def checkNumUses(user, numUses):
        if check current number of qr visits >= numUses

    def changeTimeLeft(user, timeMin):
        timeInSeconds = timeMin * 60
        countdownToRemove(timeInSeconds)

    def countdownToRemove(timeSec)
        
        while timeSec:
            minute, second = divmod(timeSec, 60)
            timer = '{:02d}:{:02d}'.format(minute, second)
            time.sleep(1)
            timeSec -= 1

        user.deleteQR()
    
