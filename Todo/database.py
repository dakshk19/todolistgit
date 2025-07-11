from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_url = f"sqlite:///./task.db"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

sessionlocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base() 

def get_db():

    db = sessionlocal()

    try:
        yield db

    finally:

        db.close()