import qrcode
from qrcode import constants

qr = qrcode.make('alphabet')



qr = qrcode.QRCode(


    version=1,
    box_size=15,
    border=5


)


data = 'wellford.nft'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color=(255, 0, 0), back_color=(0, 0, 255))
img.save('site.png')


