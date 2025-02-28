import imaplib
import os
import email

from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
IMAP_SERVER = "imap.gmail.com"
PORT = 993


def retrieve_email(sender: str, subject: str):
    found_emails = []
    try:
        with imaplib.IMAP4_SSL(IMAP_SERVER, PORT) as mail:
            mail.login(EMAIL, APP_PASSWORD)
            mail.select("Inbox")
            status, data = mail.search(None, f"(From \"{sender}\")", f"(Subject \"{subject}\")")
            if status == "OK":
                email_ids = data[0]
                for email_id in email_ids.split():
                    status, data = mail.fetch(email_id, "(RFC822)")
                    if status == "OK":
                        for response_part in data:
                            if isinstance(response_part, tuple):
                                msg = email.message_from_bytes(response_part[1])
                                found_emails.append(msg)
        return found_emails
    except Exception as e:
        print(f"Error: {e}")
