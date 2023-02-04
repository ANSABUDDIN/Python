import qrcode
from PIL import Image
# normal code

# img = qrcode.make("https://pypi.org/project/qrcode/")
# img.save("ansab_vg.png")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,
                   border=1,
                   )
qr.add_data("https://pypi.org/project/qrcode/")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("ansab_newLogo.png") 