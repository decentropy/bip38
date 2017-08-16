from bip38 import *
from bitcoin import *


print 'BIP38 Unlock: decrypt private key from passphrase encrypted key.'
print "====="
print "(Always ensure security and privacy before exposing private keys)"

print " "
print 'Enter BIP38 encrypted key:'
bip = raw_input()

print " "
print 'Enter secret passphrase:'
pasw = raw_input()
print " "

#decrypt
wif = bip38_decrypt(bip, pasw)

print "Address: " + privtoaddr(wif)
print "Key: " + wif
print " "

