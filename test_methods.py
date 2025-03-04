import os

from dotenv import load_dotenv

from send_email import send_email
from retrieve_email import retrieve_email


load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
SUBJECT = "PythonSMTPClient"
BODY = "This email has been send by Python SMTP Client."


def test_send_email():
    result = send_email(EMAIL_ADDRESS, SUBJECT, BODY)

    assert result is True


def test_retrieve_email():
    has_image = False
    image_header = "image/jpeg"
    plain_text_header = "text/plain"

    msg = retrieve_email(EMAIL_ADDRESS, SUBJECT)

    assert msg is not None
    assert msg.get("From") == EMAIL_ADDRESS
    assert msg["Subject"] == SUBJECT

    for part in msg.walk():  # Iterate through all parts of the email message.
        if part.get_content_type() == plain_text_header:
            body_retrieved = part.get_payload(decode=True).decode()  # Extract and decode the plain text body.
            assert body_retrieved == BODY
        elif part.get_content_type() == image_header:
            has_image = True
            assert has_image is True
