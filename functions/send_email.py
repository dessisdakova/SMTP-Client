import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication

from dotenv import load_dotenv


SERVER = "smtp.gmail.com"
PORT = 587  # TLS
load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
IMAGE_PATH = os.getenv("IMAGE_PATH")
DOC_PATH = os.getenv("DOC_PATH")


def send_email(recipient: str, subject: str, body: str, attachment_path: str=None) -> bool:
    e_message = _construct_email_message(recipient, subject, body, attachment_path)
    if e_message:
        try:
            with smtplib.SMTP(SERVER, PORT) as server:
                server.starttls()
                server.login(EMAIL, APP_PASSWORD)
                server.sendmail(EMAIL, recipient, e_message.as_string())  # Convert MIMEMultipart object to a string.
                return True

        except Exception as e:
            print(f"Error with server: {e}")
            return False
    else:
        return False

def _construct_email_message(recipient: str, subject: str, body: str, attachment_path: str=None):
    """Construct the email object that will be sent."""
    try:
        msg = MIMEMultipart()

        msg.add_header("From", EMAIL)
        msg.add_header("To", recipient)
        msg.add_header("Subject", subject)

        msg.attach(MIMEText(body))

        if attachment_path is not None:
            try:
                with open(attachment_path, "rb") as file:
                    file_data = file.read()
                    file_name = os.path.basename(attachment_path)
                    _, file_extension = os.path.splitext(attachment_path)
                    if file_extension.lower() in (".jpg", ".jpeg", ".png", ".gif"):
                        msg.attach(MIMEImage(file_data, name=file_name))
                    elif file_extension.lower() in (".mp3", ".wav"):
                        msg.attach(MIMEAudio(file_data, name=file_name))
                    else:
                        msg.attach(MIMEApplication(file_data, name=file_name))
            except FileNotFoundError:
                print(f"Error: Attachment file not found at {attachment_path}")
                return None
    except Exception as e:
        print(f"Error with constructing email message: {e}")
        return None

    return msg

send_email(EMAIL, "test", "test", DOC_PATH)