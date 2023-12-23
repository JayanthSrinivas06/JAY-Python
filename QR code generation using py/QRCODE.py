import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make("Welcome to Javatpoint.")  
# saving the image file  
qr_img.save("qr-img.jpg") 
