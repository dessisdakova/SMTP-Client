import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
IMAGE_PATH = os.getenv("IMAGE_PATH")
SMTP_SERVER = "smtp.gmail.com"
PORT = 587  # TLS


def send_email(recipient: str, subject: str, body_text: str) -> bool:
    try:
        msg = MIMEMultipart()  # Create container object.

        msg["From"] = EMAIL  # Add essential headers, represented as a dictionary.
        msg.add_header("To", recipient)
        msg.add_header("Subject", subject)

        body = MIMEText(body_text)  # Create an object to represent the plain text body.
        msg.attach(body)  # Attach body to message.

        try:
            with open(IMAGE_PATH, "rb") as path:  # Open image in read binary mode.
                image = MIMEImage(path.read())  # Create an object to represent the image.
                msg.attach(image)  # Attach image to message.
        except FileNotFoundError:
            print(f"Error: Image file not found at {path}")
            return False

        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            server.login(EMAIL, APP_PASSWORD)
            server.sendmail(EMAIL, recipient, msg.as_string())  # Convert MIMEMultipart object to a string.
            return True

    except Exception as e:
        print(f"Error: {e}")
        return False
