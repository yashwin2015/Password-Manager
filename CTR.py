from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import base64
import sys
import os
import binascii



class caseCTR(object):
    def __init__(self):

        # Pick randome 64-bit nonce
        self.nonce = Random.new().read(8)
        # 32-bit private key
        self.key = '1234qwerasdfzxcv5678yuiohjklnm,.'


    def encrypt(self, plaintext):
        encryptor = AES.new(self.key, AES.MODE_CTR, counter=Counter.new(64, prefix=self.nonce))
        ciphertext = base64.b64encode(encryptor.encrypt(plaintext))
        return ciphertext


    # ciphertext and nonce are taken from file
    def decrypt(self, ciphertext, nonce):
        decryptor = AES.new(self.key, AES.MODE_CTR, counter=Counter.new(64, prefix=nonce))
        plaintext = decryptor.decrypt(base64.b64decode(ciphertext))
        return plaintext