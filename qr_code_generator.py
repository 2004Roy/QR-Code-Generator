import qrcode
import image

qr=qrcode.QRCode(
    version=15,   # 15 means the version of the qr code. High the number, bigger the image
    box_size=10,  # Size of the box where the qr code will be displayed
    border=5  # it is the white part of the image-- border in all 4 sides with white color
)

data="https://www.youtube.com/watch?v=UrsmFxEIp5k&t=39081s"

qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black", back_color="white")
image.save("test.png")