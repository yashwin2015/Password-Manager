from Crypto.Cipher import AES
import os
from ECB import *
class select:
    def Selecttype(self,x,key,Value):
        if x==1:
            print str(x)+','+key+','+Value
            y=caseECB()
            key=y.encrypt(key)
            Value=y.encrypt(Value)
            return key,Value
        

    
    
        
        
        
        