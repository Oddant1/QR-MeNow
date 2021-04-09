import qrcode
import os
class profile:
    def __init__(self,first_name, last_name, phone_number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def generateQR(self):
        qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4 )
        qr.add_data(self.first_name + "\n")
        qr.add_data(self.last_name + "\n")
        qr.add_data(self.phone_number + "\n")
        qr.add_data(self.address + "\n")
        qr.add_data(self.email + "\n")
        qr.make(fit = True)
        img = qr.make_image(fillcolor = "black", back_color = "white")
        img.save(f'qrcodes/{self.first_name}.png')

    def deleteQR(self):
        if os.path.exists(f'qrcodes/{self.first_name}.png'):
            os.remove(f'qrcodes/{self.first_name}.png')
            print("Qr code removed")
        else:
            print("Qr code not found")

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getPhoneNumber(self):
        return self.phone_number

    def getAddress(self):
        return self.address

    def getEmail(self):
        return self.email

    def updateFirstName(self, updated_first_name):
        self.first_name = updated_first_name

    def updateLastName(self, updated_last_name):
        self.last_name = updated_last_name

    def updatePhoneNumber(self, updated_phone_number):
        self.phone_number = updated_phone_number

    def updateAddress(self, updated_address):
        self.address = updated_address
