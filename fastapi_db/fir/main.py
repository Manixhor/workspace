from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Create FastAPI app
app = FastAPI()

# Database setup (SQLite)
DATABASE_URL = "sqlite:///./mydata.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for tables
Base = declarative_base()

# ✅ Student table (has primary key!)
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)  # primary key here!
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

@app.post("/add-student/")
def add_student(name: str, age: int):
    db = SessionLocal()
    new_student = Student(name=name, age=age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    return {"message": f"Student {name} added!"}

@app.get("/students/")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students
