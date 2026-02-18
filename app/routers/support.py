import os
import smtplib
from email.mime.text import MIMEText
from fastapi import APIRouter
from dotenv import load_dotenv
from app.schemas import SupportMessage

load_dotenv()

router = APIRouter(prefix="/support", tags=["Support"])

@router.post("/")
def send_support_email(data: SupportMessage):
    msg = MIMEText(data.message)
    msg["Subject"] = data.subject
    msg["From"] = data.email
    msg["To"] = "karotiimars@yandex.ru"

    with smtplib.SMTP_SSL("smtp.yandex.ru", 465) as server:
        server.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
        server.sendmail(data.email, "karotiimars@yandex.ru", msg.as_string())

    return {"message": "Сообщение отправлено поддержке"}
