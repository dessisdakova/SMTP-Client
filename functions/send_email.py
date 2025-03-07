import os
import smtplib
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from typing import Optional

from helpers.constants import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, APP_PASSWORD


def send_email(recipient: str, subject: str, body: str, attachment_path: str = None) -> bool:
    """Construct an email message, open connection to the SMTP server and send an email."""
    e_message = _construct_email_message(recipient, subject, body, attachment_path)
    if e_message is None:
        return False

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, e_message.as_string())  # Convert MIMEMultipart object to a string.
            return True
    except smtplib.SMTPException:
        return False


def _construct_email_message(recipient: str, subject: str, body: str, attachment_path: str = None) -> Optional[Message]:
    """Construct the email object that will be sent."""
    try:
        msg = MIMEMultipart()

        msg.add_header("From", EMAIL_ADDRESS)
        msg.add_header("To", recipient)
        msg.add_header("Subject", subject)

        msg.attach(MIMEText(body))

        if attachment_path:
            with open(attachment_path, "rb") as file:
                file_data = file.read()
                file_name = os.path.basename(attachment_path)
                _, file_extension = os.path.splitext(attachment_path)
                if file_extension.lower() in (".jpg", ".jpeg", ".png", ".gif"):
                    msg.attach(MIMEImage(file_data, name=file_name))
                else:
                    msg.attach(MIMEApplication(file_data, name=file_name))
    except Exception:
        return None

    return msg
