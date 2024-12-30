import qrcode as qr
from PIL import Image,ImageDraw
from qrcode.console_scripts import error_correction

img=qr.make("https://www.instagram.com/")
img.save("insta.png")
img1=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10,border=4)
img1.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1")
img1.make(fit=True)
img2=img1.make_image(fill_color="black",back_color="white")
img2.save("new.png")
