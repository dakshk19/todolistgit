from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas,models, database
from ..hashing import Hash

router = APIRouter(
    tags=['users']
)

get_db = database.get_db

@router.post('/user',response_model = schemas.showuser)
def create_user(request: schemas.user, db: Session = Depends(get_db)):
    new_user = models.user(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}' ,response_model = schemas.showuser)
def get_userdata(id, db :Session = Depends(get_db)):

    user = db.query(models.user).filter(models.user.id == id).first()
    return user