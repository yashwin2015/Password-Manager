from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import base64
import sys
import os
import binascii



class caseCBC:
    def __init__(self):

        # 32-bit private key
        self.key = '1234qwerasdfzxcv5678yuiohjklnm,.'
        self.block_size = 16
        self.iv = os.urandom(16)



    def encrypt(self, ptext):
        print self,ptext +'encrypt inputs'
        encrypt_mode = AES.new(self.key, AES.MODE_CBC, self.iv)
        cipher = base64.b64encode(self.iv + encrypt_mode.encrypt((self.padding(ptext))))
        print cipher +'cipher text'
        return cipher


    def decrypt(self, cipher, iv):
        cipher = base64.b64decode(cipher)
        iv = cipher[:AES.block_size]
        encrypt_mode = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = self.unpad(encrypt_mode.decrypt(cipher[AES.block_size:]))
        return plaintext


    

    def padding(self, plaintext):
        return plaintext + (((16-len(plaintext) % 16)) * 'x')


    def unpad(self, plaintext):
        return plaintext.rstrip(b'x')
a=caseCBC()
x=a.encrypt('ptext')
y=a.decrypt(x, a.iv)
print x,y
