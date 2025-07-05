import addLog
from cryptography.fernet import Fernet
import base64


with open("cipher.txt","rb") as f:
    key=f.read()
    cipher=Fernet(key)

fileHide=open("dataPas.txt","r+")

loginPas = {}
b=1
while b==1:
    a=str(input(""))
    if a=="add":
        addLog.addLog(loginPas)
        loginPasStr=str(loginPas)
        encrypted=cipher.encrypt(loginPasStr.encode())
        base64Encrypted=base64.b64encode(encrypted).decode()
        fileHide.write(base64Encrypted)
    elif a=="list":
        fileHide.seek(0)
        file=fileHide.read()
        fileDecode=base64.b64decode(file)
        decrypted=cipher.decrypt(fileDecode)
        print(decrypted.decode())
    elif a=="del":
        delLog=str(input("Login: "))
        del(loginPas[delLog])
        loginPasStr=str(loginPas)
        encrypted=cipher.encrypt(loginPasStr.encode())
        base64Encrypted=base64.b64encode(encrypted).decode()
        fileHide.write(base64Encrypted)
    elif a=="close":
        fileHide.close()
        b=0
   
        
        
      
print("Завершено")
    

