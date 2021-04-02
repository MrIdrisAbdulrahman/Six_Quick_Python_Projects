import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
data = 'Please subscribe to the channel'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit=True)
image = qr.make_image(fill_color = 'black', back_color = 'white')

image.save('/home/abdulrahman/PycharmProjects/QRCode_Encoding_and_Decoding/Image/myqrcode.png')

# Decodes the generated QR Code
image = Image.open('/home/abdulrahman/PycharmProjects/QRCode_Encoding_and_Decoding/Image/myqrcode.png')

result = decode(image)

print(result)

