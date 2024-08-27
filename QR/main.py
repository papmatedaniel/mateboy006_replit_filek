import io
import qrcode
qr = qrcode.Qrcode()
qr.add_data("Hello World")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())


"""
import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
"""