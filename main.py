import qrcode
import base64

ss_method = "aes-256-cfb"
ss_port = "443"
ss_password = "lalala"
ss_ip = "1.2.3.4"

#ss://method[-auth]:password@hostname:port
url = ss_method + ":" + ss_password + "@" + ss_ip + ":" + ss_port
print url

#ss://YmYtY2ZiOnRlc3RAMTkyLjE2OC4xMDAuMTo4ODg4
url2 = base64.b64encode(url)
encodeUrl = "ss://" + url2
print encodeUrl

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(encodeUrl)

qr.make(fit=True)
img = qr.make_image()
img.save("shadowsocks_qr.png")
