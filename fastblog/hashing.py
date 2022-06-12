from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    def encrypt(password):
        return pwd_ctx.hash(password)
    
    def verify(plain_password, hash_password):
        return pwd_ctx.verify(plain_password, hash_password)
