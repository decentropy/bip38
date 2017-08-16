from bip38 import *
from bitcoin import *
from qrcode import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import getpass

print 'BIP38 generator: Generates paper wallet, encrypted with supplied passphrase.'
print "====="

print " "
print 'Enter description for this wallet (optional):'
name = raw_input()

print " "
print 'Enter a secret passphrase:'
pasw = getpass.getpass()
if not pasw:
    print 'you must enter a passphrase'
    exit()

print " "
print 'Re-enter the passphrase:'
pasw2 = getpass.getpass()
if pasw != pasw2:
    print 'passphrase does not match'
    exit()

print " "
print 'Enter passphrase hint (recommended):'
hint = raw_input()

priv = random_key() #private key (hex)
priv2 = decode_privkey(priv,'hex') #private key (raw)'
wif = encode_privkey(priv, 'wif') #private key (WIF)

#encrypt
addr = privtoaddr(priv)
bip = bip38_encrypt(priv,pasw)

#image...
img = Image.open("background.jpg") #around 1000 x 500
img_w, img_h = img.size

#QR image for addr
qr = QRCode(box_size=8, border=3, error_correction=ERROR_CORRECT_Q) 
qr.add_data(addr)
im = qr.make_image()
im_w, im_h = im.size

#QR image for key
qr2 = QRCode(box_size=6, border=3, error_correction=ERROR_CORRECT_M) 
qr2.add_data(bip)
im2 = qr2.make_image()
im2_w, im2_h = im2.size

#draw QRs
offs = (img_w - im_w - im2_w) / 4
img.paste(im, (offs,(img_h-im_h)/2) )
img.paste(im2, (im_w+(3*offs),(img_h-im2_h)/2) )

#draw labels
draw = ImageDraw.Draw(img) 
font = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf",22)
fcolor =  (0,0,0)
draw.text((im_w+(3*offs),(img_h-im_h)/2-10), 'BIP38 Key', fcolor, font)
draw.text((20, 20), name, fcolor, font)
draw.text((20, 70), 'ADDRESS:  ' + addr, fcolor, font)
draw.text((20, (img_h - 100)), 'BIP38 KEY:  ' + bip, fcolor, font)
draw.text((20, (img_h - 50)), 'PASSPHRASE HINT:  ' + hint, fcolor, font)

img.save(addr+'.jpg', "JPEG")

print " "
print 'Bitcoin address:'
print addr
print " "
print "Paper wallet image file created..."
print " "
#print 'BIP38 encrypted key:'
#print bip

