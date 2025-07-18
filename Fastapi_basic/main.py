from fastapi import FastAPI, Depends, status
from . import schemas, models
from .database import engine, sessionlocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():

    db = sessionlocal()

    try:
        yield db

    finally:

        db.close()

@app.post('/task')
def adding_new_task(request: schemas.task, db: Session = Depends(get_db)):

    newtask = models.task(name=request.name)
    db.add(newtask)
    db.commit()
    db.refresh(newtask)
    return newtask


@app.get('/task')
def show_Todolist(db: Session = Depends(get_db)):

    tasks = db.query(models.task).all()
    return tasks

@app.put('/task/{id}')
def update_task(id, request: schemas.task , db: Session = Depends(get_db)):
    task = db.query(models.task).filter(models.task.id == id)
    task.update(request)
    db.commit()
    return 'updated'

@app.delete('/task/{id}')
def delete_task(id, db: Session = Depends(get_db)):
    db.query(models.task).filter(models.task.id == id).delete(synchronize_session=False)

    db.commit()
    return 'done'
    

