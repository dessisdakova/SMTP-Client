import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587


def send_email(recipient: str, subject: str, body_text: str) -> bool:
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        body = MIMEText(body_text, "plain")
        msg.attach(body)

        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, recipient, msg.as_string())
            return True

    except Exception as e:
        print(f"Error: {e}")
        return False
