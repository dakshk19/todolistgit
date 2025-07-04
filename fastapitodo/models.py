from sqlalchemy import Column, Integer, String
from .database import Base


class task(Base):

   __tablename__ = 'tasks'
   
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   taskstatus = Column(String)