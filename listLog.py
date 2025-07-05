import base64
from cryptography.fernet import Fernet
def listLog(f,cip):
    file=f.read()
    fileDecode=base64.b64decode(file)
    decrypted=cip.decrypt(fileDecode)
    print(decrypted.decode())
