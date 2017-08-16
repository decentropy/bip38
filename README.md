# bip38

Python 2.7 BIP38 paper wallet creator
(Credit: https://github.com/surg0r/bip38)

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

sudo apt-get install python-dev
sudo apt-get install libssl-dev
sudo apt-get install libjpeg-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libpng-dev

sudo pip install pycrypto
sudo pip install scrypt
sudo pip install bitcoin
sudo pip install base58
sudo pip install pillow
