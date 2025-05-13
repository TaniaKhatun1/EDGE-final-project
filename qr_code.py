import qrcode as qr

#Date to be encoded
data = "Hi! My Name is Tania."

#Creating an instance of QRCode
qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#Adding data to the QRCode instance 
qr_code.add_data(data)
qr_code.make(fit=True)

#Creating an image from the QRCode instance
img = qr_code.make_image(fill_color="black", back_color="pink")
img.show()  # Display the image
