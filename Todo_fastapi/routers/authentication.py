from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..import models ,schemas, database, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(database.get_db)):
    user = db.query(models.user).filter(models.user.email == request.username).first()
    if not user:
        return 'invalid credentials'

    if not Hash.verify(user.password, request.password):
        return 'incorrect passkey'

    access_token = token.create_access_token(data={"sub": user.email})
    return schemas.token(access_token = access_token, token_type="bearer")
