import qrcode

print('Welcome to the QrCodeGenerator')
data= input("Please Enter the Website Address : ")
qr=qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')