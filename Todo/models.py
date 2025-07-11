from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class task(Base):

   __tablename__ = 'tasks'
   
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   taskstatus = Column(String)
   user_id = Column(Integer,ForeignKey('users.id'))

   username = relationship("user", back_populates = "taskname")

class user(Base):

   __tablename__ = 'users'

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   email = Column(String)
   password =  Column(String)

   taskname = relationship("task", back_populates = "username")

