from bip38 import *
from bitcoin import *
from qrcode import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import getpass

print "==============================================================="
print ' BIP38 generator: Create paper wallet, encrypted with passphrase.'
print "==============================================================="

print " "
print 'Enter description for this wallet (optional):'
name = raw_input()

print " "
print 'Enter a WIF format private key (optional):'
wif = raw_input()
if not wif:
    #randomkey = binascii.hexlify(os.urandom(32)).decode()
    wif = encode_privkey(random_key(), 'wif') #private key (WIF)
    print("* generated new key *")

addr = privtoaddr(wif)

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

#encrypt
bip = bip38_encrypt(wif, pasw)

print " "
print 'Enter passphrase hint (recommended):'
hint = raw_input()

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
print "==============================================================="
print " Encrypted paper wallet (image file) created."
print " "
print 'Bitcoin address:' + addr
print 'Encrypted key:' + bip
print " "
print " (To decrypt, run 'python unlock-bip38.py')"
print "==============================================================="
