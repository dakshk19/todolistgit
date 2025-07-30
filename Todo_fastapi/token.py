from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas
import cred

SECRET_KEY = f"{cred.secretkey}"
ALGORITHM = f"{cred.algo}"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        token_data = schemas.tokendata(email=email)
    except JWTError:
        return 'credential problem'