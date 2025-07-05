import ast
from cryptography.fernet import Fernet
import base64
def delLog(f,cip):
    findDel=str(input("Login: "))
    f.seek(0)
    for line in f:
        line=line.strip()
        if not line:
            continue
        fileDecode=base64.b64decode(line)
        decrypted=cip.decrypt(fileDecode)       
        a=decrypted.decode()
        b=ast.literal_eval(a)
        if b.keys == findDel:
            del(b[finDel])
