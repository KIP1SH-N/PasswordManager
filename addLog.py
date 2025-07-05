from cryptography.fernet import Fernet
import base64
def addLog(f,cip):
    a=str(input("Login: "))
    b=str(input("Password: "))
    full = {a:b}
    fullstr=str(full)
    fileEncrypted = cip.encrypt(fullstr.encode())
    fileBase64=base64.b64encode(fileEncrypted).decode()
    f.write(fileBase64 + "\n")
    
    print("Success")

