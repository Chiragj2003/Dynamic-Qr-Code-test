# import qrcode



# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )


# qr.add_data('Some data')
# qr.make(fit=True)


# color1="black"
# color2="white"
# img = qr.make_image(fill_color=color1, back_color=color2)


# img.save("qr-img.jpg")  


import qrcode
from PIL import Image

def generate_qr_basic(data, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

data = "https://example.com"
img = generate_qr_basic(data, fill_color="blue", back_color="white")
img.save("logo.png")
