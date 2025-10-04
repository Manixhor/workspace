from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sesssionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blod.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args = {"check_same_thread":False})



SessionLocal = sesssionmaker(bind=engine, autocommit = False, autoflush=False,)
Base = declarative_base()


