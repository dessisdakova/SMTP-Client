import email
import imaplib
import os
from email.message import Message
from functools import wraps
from typing import Callable, Any, Optional

from dotenv import load_dotenv


SERVER = "imap.gmail.com"
PORT = 993
load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def imap_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """A decorator to establish connection to an IMAP server and perform login."""
    @wraps(func)  # preserve original function's metadata
    def wrapper(*args, **kwargs):
        try:
            with imaplib.IMAP4_SSL(SERVER, PORT) as mail:
                mail.login(EMAIL, APP_PASSWORD)
                return func(mail, *args, **kwargs)  # pass the mail object as additional parameter
        except Exception as e:
            print(f"Error: {e}")
            return False
    return wrapper


@imap_decorator
def retrieve_email(mail: imaplib.IMAP4_SSL,
                   by_sender: str, by_subject: str, by_mailbox: str = "Inbox") -> Optional[Message]:
    """Retrieve an email (email.message.Message objects) after performing a search by criteria

    :param mail: Should NOT be passed when calling the function. A decorator passes it.
    :param by_sender: Sender's email address you want to search for.
    :param by_subject: Email subject you want to search for.
    :param by_mailbox: Mailbox you want to search in.
    """
    try:
        mail.select(by_mailbox)
        status, data = mail.search(None,
                                   f"(FROM \"{by_sender}\")", f"(SUBJECT \"{by_subject}\")")
        if status == "OK":
            email_ids = data[0].split()
            for id_ in email_ids:
                status, data = mail.fetch(id_, "(RFC822)")
                if status == "OK":
                    for part in data:
                        if isinstance(part, tuple):
                            return email.message_from_bytes(part[1])
    except Exception as e:
        print(f"Error with searching and fetching email: {e}")
        return None
