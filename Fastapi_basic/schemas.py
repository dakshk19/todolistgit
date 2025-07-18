from pydantic import BaseModel

class task(BaseModel):

    name: str
    taskstatus: str