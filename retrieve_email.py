import imaplib
import os
import email
from email.message import Message
from typing import Optional

from dotenv import load_dotenv


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
IMAP_SERVER = "imap.gmail.com"
PORT = 993


def retrieve_email(sender: str, subject: str) -> Optional[Message]:
    try:
        with imaplib.IMAP4_SSL(IMAP_SERVER, PORT) as mail:
            mail.login(EMAIL, APP_PASSWORD)
            mail.select("Inbox")  # Select a mailbox to fetch from.
            status, data = mail.search(None, f"(From \"{sender}\")", f"(Subject \"{subject}\")")
            if status == "OK":
                email_id = data[0].split()[0]  # Take only the first ID in case there is more than one result.
                status, data = mail.fetch(email_id, "(RFC822)")  # Fetch entire email.
                if status == "OK":
                    for response_part in data:
                        if isinstance(response_part, tuple):  # Email is in the tuple.
                            return email.message_from_bytes(response_part[1])  # Convert byte string to an object.
    except Exception as e:
        print(f"Error: {e}")
