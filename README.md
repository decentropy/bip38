# BIP38 Paper Wallet Creator

BIP38 is a protocol which encrypts a bitcoin private key with a pass phrase (using AES and scrypt), such that 
brute forcing will be very difficult / time consuming. It is used at sites like bitcoinpaperwallet.com and 
bitaddress.org, and works with several wallet apps.

**create-bip38.py** (create paper wallet)
- minimal code, easy to verify
- randomly generates new bitcoin address/key
- emits image file with encrypted key (avoids spyware)

**unlock-bip38.py** (decrypt for key)
- decrypt private key from passphrase and encrypted key

![terminal](https://raw.githubusercontent.com/steve-vincent/bip38/master/screens/terminal.png)

![sample](https://raw.githubusercontent.com/steve-vincent/bip38/master/screens/sample.jpg)

**Requirements**

Python 2.7

Required packages
sudo apt-get install python-dev libssl-dev libjpeg-dev zlib1g-dev libpng-dev libfreetype6-dev

Required modules
sudo pip install pycrypto scrypt bitcoin base58 pillow


(Credit: https://github.com/surg0r/bip38)
