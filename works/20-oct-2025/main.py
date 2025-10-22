from fastapi import FastAPI, BackgroundTasks
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load Gmail info
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

app = FastAPI()

def send_email(to: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to

    # connect to Gmail's mail server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # 🔒 make it secure
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
    print(" Email sent!")

@app.get("/send-mail/")
def send_mail(background_tasks: BackgroundTasks, to: str):
    background_tasks.add_task(send_email, to, "Hello from FastAPI!", "Hi! This is your FastAPI app saying hello")
    return {"message": "Email is being sent in the background!"}
