import ast
from cryptography.fernet import Fernet
import base64
def listLog(f,cip):
    f.seek(0)
    for line in f:
        line=line.strip()
        if not line:
            continue
        fileDecode=base64.b64decode(line)
        decrypted=cip.decrypt(fileDecode)        
        print(decrypted.decode())
        
        
    
