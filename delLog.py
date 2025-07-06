import ast
from cryptography.fernet import Fernet
import base64
def delLog(f,cip):
    findDel=str(input("Login: "))
    f.seek(0)
    colle={}
    for line in f:
        line=line.strip()
        if not line:
            continue
        fileDecode=base64.b64decode(line)
        decrypted=cip.decrypt(fileDecode)       
        a=decrypted.decode()
        b=ast.literal_eval(a)        
        colle.update(b)
    del(colle[findDel])
    f.seek(0)
    f.truncate()
    colleStr=str(colle)
    fileEncrypted=cip.encrypt(colleStr.encode())
    fileBase64=base64.b64encode(fileEncrypted).decode()
    f.write(fileBase64 + "\n")
    print("Success")
    
    
