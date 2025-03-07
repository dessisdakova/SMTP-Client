import imaplib
from functools import wraps
from typing import Callable, Any


def imap_decorator(host: str, port: int, email: str, password: str):
    """A decorator to establish connection to an IMAP server and perform login."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)  # preserve original function's metadata
        def wrapper(*args, **kwargs):
            try:
                with imaplib.IMAP4_SSL(host, port) as mail:
                    mail.login(email, password)
                    return func(mail, *args, **kwargs)  # pass the mail object as additional parameter
            except Exception as e:
                print(f"Error: {e}")
                return False
        return wrapper
    return decorator
