import os
import binascii
from bitcoin import *

#this script is a simple vanity address creator

#prefix to match (suggest <5 chars, with no l,1,0,O)
match = ["1HDL"]

looking=True
while(looking):  
  wif = encode_privkey(random_key(), 'wif')
  addr = privtoaddr(wif)
  if (addr[0:len(match[0])] in match):
    print(wif)
    print(addr)
    looking=False
