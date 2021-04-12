from userProfileHandler import *
import userProfile
import time


class controller:
    firstName = userProfile.getFirstName()
    lastName = userProfile.getLastName()
    phone = userProfile.getPhoneNumber()
    address = userProfile.getAddress()
    email = userProfile.getEmail()

    user = makeUserProfile(firstName, lastName, phone, address, email)

    def pauseCode(user):
        user.deleteQR()

    def resumeCode(user):
        user.generateQR()

    def changeTimeRemaining(user, timeMin):
        timeInSeconds = timeMin * 60
        countdownToRemove(timeInSeconds)

    def countdownToRemove(timeSec):
        while timeSec > 0:
            minute, second = divmod(timeSec, 60)
            timer = '{:02d}:{:02d}'.format(minute, second)
            time.sleep(1)
            timeSec -= 1

        user.deleteQR()
