from Crypto.Cipher import AES
from Crypto import Random
import binascii
import sys
import os
from argparse import OPTIONAL

class caseECB(object):
    def __init__(self):
        self.key="1234qwerasdfzxcv5678yuiohjklnm,."
    def encrypt(self,ptext):
        encrypt_mode= AES.new(self.key,AES.MODE_ECB)
        cipher=encrypt_mode.encrypt(self.padding(ptext))
        cipher=cipher.encode('hex')
        return cipher
    def decrypt(self,cipher):
        cipher=binascii.unhexlify(cipher)
        encrypt_mode=AES.new(self.key,AES.MODE_ECB)
        ptext=self.unpad(encrypt_mode.decrypt(cipher))
        return ptext
    def padding(self,plaintext):
        return plaintext + (((16-(len(plaintext) % 16))) * 'x')
    def unpad(self,plaintext):
        return plaintext.rstrip(b'x')   

