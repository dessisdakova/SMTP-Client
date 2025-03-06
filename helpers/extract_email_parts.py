from typing import Optional


def get_sender(msg) -> str:
    """Get 'FROM' header of an email."""
    return msg.get("From")


def get_subject(msg) -> str:
    """Get 'SUBJECT' header of an email."""
    return msg.get("Subject")


def get_body(msg) -> Optional[str]:
    """Get plain text body of an email."""
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            return part.get_payload(decode=True).decode()


def get_attachment_name(msg) -> Optional[str]:
    """Get attachment name of an email if applicable, else returns 'None'."""
    content_types = ("image/jpeg", "application/octet-stream")
    for part in msg.walk():
        c_type = part.get_content_type()
        if c_type in content_types:
            file_name = part.get_filename()
            return file_name
