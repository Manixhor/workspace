#integrating mail in FastAPI 
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig 
from pydantic import BaseModel, EmailStr

app = FastAPI()
conf = ConnectionConfig(
    MAIL_USERNAME = "manixhorpb@gmail.com"
    MAIL_PASSWORD = ""
)


