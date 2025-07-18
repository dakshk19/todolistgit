from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import schemas, models, database,oauth2

router = APIRouter(
    tags = ['tasks']
)

get_db = database.get_db

@router.post('/task')

def adding_new_task(request: schemas.task, db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):

    newtask = models.task(name=request.name,taskstatus= request.taskstatus)
    db.add(newtask)
    db.commit()
    db.refresh(newtask)
    return newtask

@router.get('/task')
def show_Todolist(db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):

    tasks = db.query(models.task).all()
    return tasks

@router.put('/task/{id}')
def update_task(id, request: schemas.task , db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    task = db.query(models.task).filter(models.task.id == id).update(dict(request))
    db.commit()
    return 'updated'

@router.delete('/task/{id}')
def delete_task(id, db: Session = Depends(get_db),current_user: schemas.user = Depends(oauth2.get_current_user)):
    db.query(models.task).filter(models.task.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'