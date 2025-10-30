from databse import Base
from sqlalchemy import column, Integer, String

class Blog(Base):
    id = column(Integer,primary_key = True, index = True)
    title = column(String)
    body = column(String)


    