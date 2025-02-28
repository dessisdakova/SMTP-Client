import os

from dotenv import load_dotenv

from send_email import send_email
from retrieve_email import retrieve_email


load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
SUBJECT = "PythonSMTPClient"
BODY = "This email has been send by Python SMTP Client."


def test_sending_email():
    result = send_email(EMAIL_ADDRESS, SUBJECT, BODY)

    assert result is True


def test_retrieving_email():
    results = retrieve_email(EMAIL_ADDRESS, SUBJECT)

    assert len(results) != 0
    assert results[0]["From"] == EMAIL_ADDRESS
    assert results[0]["Subject"] == SUBJECT
    for part in results[0].walk():
        no_header = "text/plain"
        if part.get_content_type() == no_header:
            body_retrieved = part.get_payload(decode=True).decode()
            assert body_retrieved == BODY
