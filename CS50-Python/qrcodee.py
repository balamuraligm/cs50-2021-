import os
import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=ZEQh45W_UDo")

img.save('qr.png', "PNG")


os.system("open qr.png")

os.system("open DIK_8499.JPG")



