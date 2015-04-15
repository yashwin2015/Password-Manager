from Crypto.Cipher import AES
import csv
import sys
from ECB import *
from SelectCrypcto import *
from CBC import caseCBC

from CTR import caseCTR
dic={}
dict={}
#function to write data to a file
def Selecttype(x,key):
    print 'selcet type 1 called'
    if x == str(1):
        y=caseECB()
        key=y.encrypt(key)
    elif x == str(2):
        y=caseCBC()
        key=y.encrypt(key)
        print key +'selectype function o/p'
    elif x == str(3):
        y=caseCTR()
        key=y.nonce+':'+y.encrypt(key)
    return key
def Selecttype2(x,cipher):
    
    if x == str(1):
        y=caseECB()
        key=y.decrypt(cipher)
        
    elif x == str(2):
        y=caseCBC()
        key=y.decrypt(cipher,y.iv)
        
    elif x == str(3):
        y=caseCTR()
        nonce=cipher.split(":")[0]
        cipher=cipher.split(":")[1]
        key=y.decrypt(cipher,nonce)
    return key
        
def writefile():
        print 'writedta called'
        while (True) :
            x=raw_input('give username\n')
            y=raw_input('give password\n')
            z=raw_input('give 1 for ECB mode 2 for CBC 3 for ctr\n')
            if x=='' or y=='':
                print 'please make shure you have given both username and password\n'
                k= raw_input('to exit give exit else no')
                if k=='exit':sys.exit(0)
            else:
                break
                
                
        en_x= Selecttype(z, x)
        en_y=Selecttype(z, y)
        if z==str(1):
            rFile=open('textfileECB.csv','r')
            wfile=open('textfileECB.csv','a')
            print 1
            
        elif z==str(2):
            rFile=open('textfileCBC.csv','r')
            wfile=open('textfileCBC.csv','a')
            print 2
        elif z==str(3):
            rFile=open('textfileCTR.csv','r')
            wfile=open('textfileCTR.csv','a')
            print 3
        else:
            print 'wrong encrypt type'
            return
        for key,val in csv.reader(rFile):
            print key
            if Selecttype2(z, key)==x:
                print"user name exists"
                sys.exit()
          
        dic[x]=y
        w=csv.writer(wfile)
        w.writerow([en_x,en_y])
        print x,y
        print"done"
#function to getdata from file
def fetchdata():
        print'fetch data called'
        z=raw_input('give username')
        y=raw_input('give encryption mode 1 for ecb 2 for cbc 3 for ctr')
       
        if y==str(1):
            rFile=open('textfileECB.csv','r')
            print 1
            
        elif y==str(2):
            rFile=open('textfileCBC.csv','r')
            print 2
        elif y==str(3):
            rFile=open('textfileCTR.csv','r')
            print 3
        else:
            print 'wrong encrypt type'
            return
        try:
            for key,val in csv.reader(rFile):
                key=Selecttype2(y,key)
                val=Selecttype2(y,val)
                if key==z: 
                    print key+':'+val       
        except:
            print'not found'
#mainprogram
for a in range(5):
    x= raw_input('give master password to proceed')
    if x=='Monster':
        while(True):
            x=raw_input('give 1 to save value and 2 to check value and 3 to exit\n')
            if x=='1':writefile()
            elif x=='2':fetchdata()
            elif x=='3':sys.exit(0)
    else:print"wrong password %d of 5 attempt"%(a+1) 
else:
    w=open('textfileCBC.csv','w')
    w.write('')
    w.close()
    
    w=open('textfileCTR.csv','w')
    w.write('')
    w.close()
    
    w=open('textfileECB.csv','w')
    w.write('')
    w.close()
    print"too many wrong attempts data crashed"
    sys.exit(0)