import email
import imaplib
from email.message import Message
from typing import Optional

from functions.imap_decorator import imap_decorator
from helpers.constants import IMAP_SERVER, IMAP_PORT, EMAIL_ADDRESS, APP_PASSWORD


@imap_decorator(IMAP_SERVER, IMAP_PORT, EMAIL_ADDRESS, APP_PASSWORD)
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
    except Exception:
        return None
