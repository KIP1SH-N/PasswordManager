import addLog
import listLog
import delLog
from cryptography.fernet import Fernet
import base64

with open("cipher.txt","rb") as f:
    key=f.read()
    cipher=Fernet(key)

fileHide=open("dataPas.txt","r+")
b=1
print(" add - add login and password \n list - show all data \n close - finish program")
while b==1:
    a=str(input(""))
    if a=="add":
        addLog.addLog(fileHide,cipher)
    elif a=="list":
        listLog.listLog(fileHide,cipher)
    elif a=="del":
        delLog.delLog(fileHide,cipher)
    elif a=="close":
        fileHide.close()
        b=0
        
   
        
        
      
print("Finish")
    

