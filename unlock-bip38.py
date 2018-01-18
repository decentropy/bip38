from bip38 import *
from bitcoin import *


print "==============================================================="
print ' BIP38 Unlock: decrypt a passphrase encrypted private key.'
print " (Always protect your private keys!)"
print "==============================================================="

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

