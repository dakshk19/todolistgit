from pydantic import BaseModel
from typing import List, Optional

class task(BaseModel):

    name: str
    taskstatus: str

class showuser(BaseModel):

    name: str
    email:str
    tasks: List[task] = []

    class config:

        orm_mode=True

class showtask(BaseModel):

    name: str
    taskstatus: str
    user: showuser

    class config:
        orm_mode=True

class user(BaseModel):

    name: str
    email:str
    password: str

class token(BaseModel):
    access_token: str
    token_type: str
    
class tokendata(BaseModel):
    username: Optional[str] = None