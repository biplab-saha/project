import qrcode

#Taking UPI ID As a input
upiId = input("Enter your UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# difining the payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support

phonepeUrl = f'upi://pay?pa={upiId}&pn=Recipient%20Name&mc=1234'
paytmUrl = f'upi://pay?pa={upiId}&pn=Recipient%20Name&mc=1234'
googlePayUrl = f'upi://pay?pa={upiId}&pn=Recipient%20Name&mc=1234'

# Create QR codes for each payment app
phonepeQr=qrcode.make(phonepeUrl)
paytmQr=qrcode.make(paytmUrl)
googlePayQr=qrcode.make(googlePayUrl)

# save the Qr code to image file (optional)
# phonepeQr.save('phonepeQr.png')
# paytmQr.save('paytmQr.png')
# googlePayQr.save('googlePayQr.png')


#display the Qr code (you may need to install pil/pillow library)
phonepeQr.show()
# paytmQr.show()
# googlePayQr.show()


