import qrcode
import os


class profile:

    def __init__(self, first_name, last_name, phone_number, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def generate_qr(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(self.first_name + "\n")
        qr.add_data(self.last_name + "\n")
        qr.add_data(self.phone_number + "\n")
        qr.add_data(self.address + "\n")
        qr.add_data(self.email + "\n")
        qr.make(fit=True)
        img = qr.make_image(fillcolor="black", back_color="white")
        img.save(f'qrcodes/{self.first_name}.png')

    def delete_qr(self):
        if os.path.exists(f'qrcodes/{self.first_name}.png'):
            os.remove(f'qrcodes/{self.first_name}.png')
            print("Qr code removed")
        else:
            print("Qr code not found")

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def update_first_name(self, updated_first_name):
        self.first_name = updated_first_name

    def update_last_name(self, updated_last_name):
        self.last_name = updated_last_name

    def update_phone_number(self, updated_phone_number):
        self.phone_number = updated_phone_number

    def update_address(self, updated_address):
        self.address = updated_address
