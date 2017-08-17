# BIP38 Paper Wallet Creator

BIP38 is a protocol which encrypts a bitcoin private key with a passphrase (using AES and scrypt), such that 
brute forcing will be very difficult / time consuming. BIP38 works with several wallet apps, and is used at sites
like bitcoinpaperwallet.com and bitaddress.org. This python 2.7 script generates BIP38 encrypted paper wallets.
This is a safe storage method, secured with a passphrase even if a stranger found it.

**create-bip38.py** (create paper wallet)
- minimal code, easy to verify
- randomly generates new bitcoin address/key
- emits image file with passphrase encrypted key (avoids spyware)

**unlock-bip38.py** (decrypt for key)
- decrypt private key from passphrase and encrypted key

![terminal](https://raw.githubusercontent.com/steve-vincent/bip38/master/screens/terminal.png)

![sample](https://raw.githubusercontent.com/steve-vincent/bip38/master/screens/sample.jpg)

**Requirements**

Python 2.7

Required packages: (apt-get install) python-dev libssl-dev libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev

Required modules: (pip install) pycrypto scrypt bitcoin base58 pillow

(Credit: https://github.com/surg0r/bip38)
