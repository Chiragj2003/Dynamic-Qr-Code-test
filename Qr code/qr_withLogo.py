import qrcode
from PIL import Image


def generate_qr_with_logo(data, logo_path, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

    logo = Image.open(logo_path)
    basewidth = int(img.size[0] / 4)
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)

    return img

data = "https://example.com"
logo_path = "logo.png"
img = generate_qr_with_logo(data, logo_path, fill_color="black", back_color="white")
img.save("qr_with_logo.png")
