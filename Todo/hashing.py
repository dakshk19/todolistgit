from passlib.context import CryptContext

passwdcxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class Hash():
    
    def bcrypt(password: str):
        return passwdcxt.hash(password)

    def verify(Hashed_pass,plain_pass):

        return passwdcxt.verify(plain_pass,Hashed_pass)